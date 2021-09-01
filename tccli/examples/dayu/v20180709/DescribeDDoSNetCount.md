**Example 1: 获取高防IP专业版资源的DDoS攻击占比分析**



Input: 

```
tccli dayu DescribeDDoSNetCount --cli-unfold-argument  \
    --Business net \
    --Id net-00000010 \
    --StartTime 2018-08-2715:05:10 \
    --EndTime 2018-08-2716:05:10 \
    --MetricName pkg
```

Output: 
```
{
    "Response": {
        "Business": "net",
        "Data": [],
        "EndTime": "2019-03-07 14:50:00",
        "MetricName": "pkg",
        "Id": "net-000000y0",
        "RequestId": "69b1692b-4b6e-47c0-a7d6-0ff0da286874",
        "StartTime": "2019-03-07 00:00:00"
    }
}
```

