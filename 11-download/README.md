# Downloading Khan academy videos for fetched youtube ids

First section takes care of downloading all Khan academy videos.
After Khan academy topic tree is parsed for YouTube video ids
the videos including subtitles are downloaded straight from YouTube.

Either download everything in serial:
```
nohup nice ./run.py > log-for-this-run &
```

Or run in arbitrary amount of batches in parralel (youtube ids are expected on standard input):
```
nohup nice ./batch.py < [YOUTUBE IDS] > > log-for-this-run &
```

**WARNING**
Downloading all Khan academy videos takes a lot of storage space
