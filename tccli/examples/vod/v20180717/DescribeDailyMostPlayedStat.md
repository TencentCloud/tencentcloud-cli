**Example 1: 查询2021-01-01 播放次数 Top100 的播放统计数据**

查询2021-01-01 播放次数 Top100 的播放统计数据

Input: 

```
tccli vod DescribeDailyMostPlayedStat --cli-unfold-argument  \
    --Date 2021-01-01T00:00:00+08:00 \
    --Metric PlayTimes
```

Output: 
```
{
    "Response": {
        "DailyPlayStatInfoSet": [
            {
                "Date": "2021-01-01T00:00:00+08:00",
                "PlayTimes": 1,
                "Traffic": 1234,
                "FileId": "5285485487985271487"
            }
        ],
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3"
    }
}
```

