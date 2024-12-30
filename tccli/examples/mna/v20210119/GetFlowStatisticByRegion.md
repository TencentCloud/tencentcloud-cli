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
                "Time": "1735259400"
            }
        ],
        "MaxValue": 0,
        "AvgValue": 0,
        "TotalValue": 0,
        "RequestId": "bd89e515-20b4-445b-a88d-7355e76f8d22"
    }
}
```

