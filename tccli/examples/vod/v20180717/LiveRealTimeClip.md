**Example 1: Temporary live clipping**



Input: 

```
tccli vod LiveRealTimeClip --cli-unfold-argument  \
    --StreamId record-stream\
    --StartTime 2018-09-20T10:00:00Z\
    --EndTime 2018-09-20T11:00:00Z
```

Output: 
```
{
    "Response": {
        "Url": "http://video.com/playlist.m3u8",
        "FileId": "",
        "VodTaskId": "",
        "MetaData": null
    }
}
```

**Example 2: Persistent live clipping**



Input: 

```
tccli vod LiveRealTimeClip --cli-unfold-argument  \
    --StreamId record-stream\
    --StartTime 2018-09-20T10:00:00Z\
    --EndTime 2018-09-20T11:00:00Z\
    --IsPersistence 1\
    --Procedure SomeProcedure
```

Output: 
```
{
    "Response": {
        "Url": "http://video.com/playlist.m3u8",
        "FileId": "",
        "VodTaskId": "",
        "MetaData": null,
        "RequestId": "requestId"
    }
}
```

