const imagemin = require('imagemin');
const imageminMozjpeg = require('imagemin-mozjpeg');
const imageminPngquant = require('imagemin-pngquant');
const path = require('path');

(async () => {
    const files = await imagemin(['images/*.{jpg,png}'], {
        destination: 'optimized-images',
        plugins: [
            imageminMozjpeg({ quality: 75 }),
            imageminPngquant({ quality: [0.6, 0.8] })
        ]
    });

    console.log('Images optimized:', files.map(file => path.basename(file.sourcePath)));
})();
