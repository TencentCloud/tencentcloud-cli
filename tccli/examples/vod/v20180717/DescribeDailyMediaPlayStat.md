**Example 1: 查询从2021-01-01到2021-01-02的媒体文件5285485487985271487的播放统计数据**



Input: 

```
tccli vod DescribeDailyMediaPlayStat --cli-unfold-argument  \
    --FileId 5285485487985271487 \
    --StartDate 2021-01-01T00:00:00+08:00 \
    --EndDate 2021-01-10T00:00:00+08:00
```

Output: 
```
{
    "Response": {
        "DailyPlayStatInfoSet": [
            {
                "FileId": "5285485487985271487",
                "Date": "2021-01-01T00:00:00+08:00",
                "PlayTimes": 13,
                "Traffic": 23434
            },
            {
                "FileId": "5285485487985271487",
                "Date": "2021-01-02T00:00:00+08:00",
                "PlayTimes": 3,
                "Traffic": 2334
            }
        ],
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3"
    }
}
```

