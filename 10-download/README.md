# Downloading all Khan academy videos

First section takes care of downloading all Khan academy videos.
This is achieved by parsing Khan academy topic tree for YouTube video ids
and then downloading these straight from YouTube (including subtitles).

```
mkdir data  # where everything will be stored
nohup nice ./run.py > log-for-this-run &
  # once the first job has downloaded data/youtube_ids.json
  # you can run as many of these jobs as you like in parallel
  # they will avoid overwriting other's work
```

**WARNING**
Downloading all Khan academy videos takes a lot of storage space
