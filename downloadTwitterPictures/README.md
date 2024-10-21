# downloadTwitterPictures

_Library to download the pictures from a given twitter account or a given hashtag._


## Basic usage

You can download the pictures for a given user as follows:

```bash
# Download 10 images from the National Geographic Twitter Account
python downloadtwitterimages.py --username NatGeoPhotos --num 10

# Download 10 images with the hashtag Photography
python downloadtwitterimages.py --hashtag Photography --num 10
```

The library also allows to include retweets or replies, and to specify a different folder to save the pictures in ("pictures" is the default)

```bash
python downloadtwitterimages.py --username cloud_images --num 10 --replies --retweets
python downloadtwitterimages.py --username cloud_images --num 10 --replies --retweets --output ../cloud_images_Pictures
python downloadtwitterimages.py --username cloud_images --num 10 --replies --retweets --config config.cfg --output ../cloud_images_Pictures
```

The library will only download pictures that are not in the output folder already to avoid duplications.

## Todo

1. Get container to run locally
    1. internet in the container isn't working for some reason.