**Example 1: 获取CC攻击指标数据**



Input: 

```
tccli dayu DescribeCCTrend --cli-unfold-argument  \
    --Business bgp \
    --Id bgp-00000010 \
    --Ip 3.3.3.3 \
    --MetricName inqps \
    --StartTime 2018-08-2715:05:10 \
    --EndTime 2018-08-2716:05:10 \
    --Period 3600
```

Output: 
```
{
    "Response": {
        "Business": "bgp",
        "Count": 1,
        "Data": [
            1234
        ],
        "EndTime": "2018-08-27 16:05:10",
        "Id": "bgp-00000010",
        "Ip": "3.3.3.3",
        "MetricName": "inqps",
        "Period": 300,
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "StartTime": "2018-08-27 15:05:10"
    }
}
```

