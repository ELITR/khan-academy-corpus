# Downloading all Khan academy videos

First section takes care of downloading all Khan academy videos.
After Khan academy topic tree is parsed for YouTube video ids
the videos including subtitles are downloaded straight from YouTube.

```
nohup nice ./run.py > log-for-this-run &
```

**WARNING**
Downloading all Khan academy videos takes a lot of storage space
