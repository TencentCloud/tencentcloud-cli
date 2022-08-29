**Example 1: 获取高防包流量折线图**



Input: 

```
tccli antiddos DescribeBgpBizTrend --cli-unfold-argument  \
    --Business xx \
    --InstanceId xx \
    --Flag 1 \
    --StartTime xx \
    --EndTime xx \
    --MetricName xx
```

Output: 
```
{
    "Response": {
        "DataList": [
            1
        ],
        "Total": 1,
        "MaxData": 1,
        "RequestId": "xx",
        "MetricName": "xx"
    }
}
```

