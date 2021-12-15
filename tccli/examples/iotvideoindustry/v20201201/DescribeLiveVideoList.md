**Example 1: 直播录像回放列表**



Input: 

```
tccli iotvideoindustry DescribeLiveVideoList --cli-unfold-argument  \
    --LiveChannelId cea6f74f29164253b43411fd888f4dc3 \
    --Offset 0 \
    --Limit 100
```

Output: 
```
{
    "Response": {
        "RecordList": [
            {
                "IntID": 3352901,
                "LiveChannelId": "cea6f74f29164253b43411fd888f4dc3",
                "ExpectDeleteTime": 1633599082,
                "RecordTimeLen": 600,
                "FileSize": 268908746,
                "VideoUrl": "https://1304886180.vod2.myqcloud.com/cac4da69vodcq1304886180/8e62c9e03701925923890211076/f0.mp4 ",
                "RecordPlanId": "plan-7fqulsjc",
                "StartTime": 1631007068,
                "EndTime": 1631007668
            }
        ],
        "RequestId": "fd344df8-6121-4e75-b417-383a67268354111",
        "Total": 1
    }
}
```

