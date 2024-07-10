**Example 1: 正常场景**



Input: 

```
tccli mna GetFlowStatisticByRegion --cli-unfold-argument  \
    --BeginTime 0 \
    --EndTime 0 \
    --Type 0 \
    --TimeGranularity 0 \
    --AccessRegion MC \
    --GatewayType 0
```

Output: 
```
{
    "Response": {
        "NetDetails": [
            {
                "Current": 0,
                "Time": "abc"
            }
        ],
        "MaxValue": 0,
        "AvgValue": 0,
        "TotalValue": 0,
        "RequestId": "abc"
    }
}
```

