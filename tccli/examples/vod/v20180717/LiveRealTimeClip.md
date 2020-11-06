**Example 1: 即时剪辑不固化**



Input: 

```
tccli vod LiveRealTimeClip --cli-unfold-argument  \
    --StreamId record-stream \
    --StartTime 2018-09-20T10:00:00Z \
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

**Example 2: 即时剪辑并且固化**



Input: 

```
tccli vod LiveRealTimeClip --cli-unfold-argument  \
    --StreamId record-stream \
    --StartTime 2018-09-20T10:00:00Z \
    --EndTime 2018-09-20T11:00:00Z \
    --IsPersistence 1 \
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

