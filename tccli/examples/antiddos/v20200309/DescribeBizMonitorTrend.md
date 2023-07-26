**Example 1: 请求入包速率**

请求入包速率

Input: 

```
tccli antiddos DescribeBizMonitorTrend --cli-unfold-argument  \
    --Business bgpip \
    --Period 60 \
    --StartTime 2023-06-21 10:00:00 \
    --EndTime 2023-06-21 10:30:00 \
    --Id bgpip-0000xbc \
    --MetricName inpkg
```

Output: 
```
{
    "Response": {
        "DataList": [
            1,
            12
        ],
        "MetricName": "inpkg",
        "MaxData": 12,
        "RequestId": "abc-as"
    }
}
```

