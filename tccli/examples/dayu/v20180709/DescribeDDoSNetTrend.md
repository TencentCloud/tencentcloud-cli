**Example 1: 获取高防IP专业版资源的DDoS攻击指标数据**



Input: 

```
tccli dayu DescribeDDoSNetTrend --cli-unfold-argument  \
    --Business net \
    --Id net-00000010 \
    --MetricName bps \
    --StartTime '2018-08-27 15:05:10' \
    --EndTime '2018-08-27 16:05:10' \
    --Period 3600
```

Output: 
```
{
    "Response": {
        "Business": "net",
        "Count": 1,
        "Data": [
            1234
        ],
        "EndTime": "2018-08-27 16:05:10",
        "Id": "net-00000010",
        "MetricName": "bps",
        "Period": 3600,
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "StartTime": "2018-08-27 15:05:10"
    }
}
```

