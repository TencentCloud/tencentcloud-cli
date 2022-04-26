**Example 1: 查询从2021-01-01 00:00:00 到2021-01-01 02:00:00的媒体文件5285485487985271487的播放统计数据**



Input: 

```
tccli vod DescribeMediaPlayStatDetails --cli-unfold-argument  \
    --FileId 5285485487985271487 \
    --StartTime 2021-01-01T00:00:00+08:00 \
    --EndTime 2021-01-01T02:00:00+08:00
```

Output: 
```
{
    "Response": {
        "PlayStatInfoSet": [
            {
                "FileId": "5285485487985271487",
                "Time": "2021-01-01T00:00:00+08:00",
                "PlayTimes": 13,
                "Traffic": 23434
            },
            {
                "FileId": "5285485487985271487",
                "Time": "2021-01-01T01:00:00+08:00",
                "PlayTimes": 3,
                "Traffic": 2334
            }
        ],
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3"
    }
}
```

