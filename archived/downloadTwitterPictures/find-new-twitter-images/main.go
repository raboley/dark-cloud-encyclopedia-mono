package main

import (
	"fmt"
	"io"
	"net/http"
	"os"
	"path/filepath"
	"sync"

	"github.com/dghubble/go-twitter/twitter"
	"github.com/dghubble/oauth1"
	"github.com/joho/godotenv"
)

// Load environment variables from .env file
func loadEnv() {
	err := godotenv.Load()
	if err != nil {
		fmt.Println("Error loading .env file")
	}
}

// Initialize Twitter client
func initTwitterClient() *twitter.Client {
	config := oauth1.NewConfig(os.Getenv("CONSUMER_KEY"), os.Getenv("CONSUMER_SECRET"))
	token := oauth1.NewToken(os.Getenv("ACCESS_TOKEN"), os.Getenv("ACCESS_SECRET"))
	httpClient := config.Client(oauth1.NoContext, token)
	return twitter.NewClient(httpClient)
}

// Fetch media URLs from tweets
func fetchMediaURLs(client *twitter.Client, username string, numTweets int) ([]string, error) {
	var mediaURLs []string
	tweets, _, err := client.Timelines.UserTimeline(&twitter.UserTimelineParams{
		ScreenName:      username,
		Count:           numTweets,
		IncludeRetweets: false,
		ExcludeReplies:  true,
		TweetMode:       "extended",
	})
	if err != nil {
		return nil, err
	}

	for _, tweet := range tweets {
		if tweet.ExtendedEntities != nil {
			for _, media := range tweet.ExtendedEntities.Media {
				mediaURLs.append(mediaURLs, media.MediaURLHttps)
			}
		}
	}
	return mediaURLs, nil
}

// Check if image is already downloaded
func isImageDownloaded(fileName string, downloadedImages map[string]bool) bool {
	_, exists := downloadedImages[fileName]
	return exists
}

// Download image
func downloadImage(url, outputFolder string, wg *sync.WaitGroup, downloadedImages map[string]bool, mu *sync.Mutex) {
	defer wg.Done()
	fileName := filepath.Base(url)
	if isImageDownloaded(fileName, downloadedImages) {
		fmt.Println("Image already downloaded:", fileName)
		return
	}

	resp, err := http.Get(url)
	if err != nil {
		fmt.Println("Error downloading image:", err)
		return
	}
	defer resp.Body.Close()

	outputPath := filepath.Join(outputFolder, fileName)
	out, err := os.Create(outputPath)
	if err != nil {
		fmt.Println("Error creating file:", err)
		return
	}
	defer out.Close()

	_, err = io.Copy(out, resp.Body)
	if err != nil {
		fmt.Println("Error saving image:", err)
		return
	}

	mu.Lock()
	downloadedImages[fileName] = true
	mu.Unlock()
	fmt.Println("Downloaded:", fileName)
}

func main() {
	loadEnv()
	client := initTwitterClient()
	username := "cloud_images"
	numTweets := 3
	outputFolder := "images"

	mediaURLs, err := fetchMediaURLs(client, username, numTweets)
	if err != nil {
		fmt.Println("Error fetching media URLs:", err)
		return
	}

	downloadedImages := make(map[string]bool)
	var wg sync.WaitGroup
	var mu sync.Mutex

	for _, url := range mediaURLs {
		wg.Add(1)
		go downloadImage(url, outputFolder, &wg, downloadedImages, &mu)
	}

	wg.Wait()
	fmt.Println("All images downloaded.")
}
