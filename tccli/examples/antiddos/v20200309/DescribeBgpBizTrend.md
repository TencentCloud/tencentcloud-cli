**Example 1: 获取高防包流量折线图**



Input: 

```
tccli antiddos DescribeBgpBizTrend --cli-unfold-argument  \
    --Business bgp-multip \
    --InstanceId bgp-00000001 \
    --Flag 1 \
    --StartTime 2022-11-29 00:00:00 \
    --EndTime 2022-11-29 01:00:00 \
    --MetricName intraffic
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
        "RequestId": "f4b3915e-c1bd-4ca4-aaef-e88eaa8aa66e",
        "MetricName": "intraffic"
    }
}
```

