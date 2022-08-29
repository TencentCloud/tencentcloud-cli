**Example 1: 即时剪辑不固化**

对直播码为 record-stream 和域名为 example.com 的直播流发起即时剪辑，起始时间为 2018-09-20T10:00:00Z，结束时间为 2018-09-20T11:00:00Z，并且不固化。假设该直播流在 2018-09-20T10:30:00Z 到 2018-09-20T10:40:00Z 存在过断流的情况，持续时间为10分钟，那么输出参数 SegmentSet 将包含两个片段信息，可以得到剪辑后的视频实际时长为50分钟。

Input: 

```
tccli vod LiveRealTimeClip --cli-unfold-argument  \
    --Host example.com \
    --EndTime 2018-09-20T11:00:00Z \
    --StartTime 2018-09-20T10:00:00Z \
    --StreamId record-stream
```

Output: 
```
{
    "Response": {
        "Url": "http://example.com/playlist.m3u8",
        "FileId": "",
        "VodTaskId": "",
        "MetaData": null,
        "SegmentSet": [
            {
                "StartTime": "2018-09-20T10:00:00Z",
                "EndTime": "2018-09-20T10:30:00Z"
            },
            {
                "StartTime": "2018-09-20T10:40:00Z",
                "EndTime": "2018-09-20T11:00:00Z"
            }
        ],
        "RequestId": "6ca31e3a-6b8e-xxxx-9256-fdc700064ef3"
    }
}
```

**Example 2: 即时剪辑并且固化**

对直播码为 record-stream 和域名为 example.com 的直播流发起即时剪辑，起始时间为 2018-09-20T12:00:00Z，结束时间为 2018-09-20T13:00:00Z，并且进行固化和发起任务流处理。

Input: 

```
tccli vod LiveRealTimeClip --cli-unfold-argument  \
    --IsPersistence 1 \
    --Host example.com \
    --StartTime 2018-09-20T12:00:00Z \
    --StreamId record-stream \
    --EndTime 2018-09-20T13:00:00Z \
    --Procedure SomeProcedure
```

Output: 
```
{
    "Response": {
        "Url": "http://example.com/playlist.m3u8",
        "FileId": "5285890xxxxxx199336",
        "VodTaskId": "125xxxx65-procedurev2-bffb15f07530b57bc1aabb01fac74bca",
        "MetaData": null,
        "SegmentSet": [
            {
                "StartTime": "2018-09-20T12:00:00Z",
                "EndTime": "2018-09-20T13:00:00Z"
            }
        ],
        "RequestId": "6ca31e3a-6b8e-xxxx-9256-fdc700064ef3"
    }
}
```

