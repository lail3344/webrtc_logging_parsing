#/bin/bash

docker exec fd7204fe029a timeout 65 google-chrome --allow-running-insecure-content --user-data-dir=/home/seluser/ --use-fake-device-for-media-stream --use-file-for-fake-audio-capture=/audio_long16_base_sound.wav https://10.239.10.4:3004 &
docker exec ba10cc6924cc timeout 65 google-chrome --allow-running-insecure-content --user-data-dir=/home/seluser/ --use-fake-device-for-media-stream --use-file-for-fake-audio-capture=/audio_long16_silence_sound.wav https://10.239.10.4:3004 &
docker exec 3b79e5a35c28 timeout 65 google-chrome --allow-running-insecure-content --user-data-dir=/home/seluser/ --use-fake-device-for-media-stream --use-file-for-fake-audio-capture=/audio_long16_silence_sound.wav https://10.239.10.4:3004 &
docker exec 08c8042f6807 timeout 65 google-chrome --allow-running-insecure-content --user-data-dir=/home/seluser/ --use-fake-device-for-media-stream --use-file-for-fake-audio-capture=/audio_long16_silence_sound.wav https://10.239.10.4:3004 &
docker exec 3c136f6cc524 timeout 65 google-chrome --allow-running-insecure-content --user-data-dir=/home/seluser/ --use-fake-device-for-media-stream --use-file-for-fake-audio-capture=/audio_long16_silence_sound.wav https://10.239.10.4:3004 &
docker exec 2e5ff0914318 timeout 65 google-chrome --allow-running-insecure-content --user-data-dir=/home/seluser/ --use-fake-device-for-media-stream --use-file-for-fake-audio-capture=/audio_long16_silence_sound.wav https://10.239.10.4:3004 &
