**Example 1: 查询2020-12-0-1到2020-12-02的播放统计文件列表**



Input: 

```
tccli vod DescribeDailyPlayStatFileList --cli-unfold-argument  \
    --StartTime 2020-12-01T00:00:00+08:00 \
    --EndTime 2020-12-02T00:00:00+08:00
```

Output: 
```
{
    "Response": {
        "PlayStatFileSet": [
            {
                "Date": "2020-12-01T00:00:00+08:00",
                "Url": "http://xxx.test.com/playstat/2021201.csv.gz?sign=abc"
            },
            {
                "Date": "2020-12-02T00:00:00+08:00",
                "Url": "http://xxx.test.com/playstat/20201202.csv.gz?sign=abc"
            }
        ],
        "RequestId": "requestId"
    }
}
```

