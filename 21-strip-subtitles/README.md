# Strip subtitles

Second section extracts audio from downloaded videos and strips subtitles of timestamps and various tags. 

Either process everything in serial:
```
nohup nice ./run.py > log-for-this-run &
```

Or run an arbitrary amount of batches in parralel (directory names with videos are expected on standard input):
```
nohup nice ./batch.py < [DIR NAMES] > log-for-this-run &
```