# FFmpeg实战
## 剪切
```
ffmpeg -ss 00:00:44.000 -t 10 -i guoliting.m4a -acodec copy output-4.m4a
```
## 合并
```
ffmpeg -i "output-1.m4a" -i "output-4.m4a" -filter_complex "[0:a][1:a]concat=n=2:v=0:a=1[out]" -map "[out]" output.m4a
```