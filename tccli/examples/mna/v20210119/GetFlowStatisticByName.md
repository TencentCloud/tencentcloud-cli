**Example 1: 根据DeviceName（test0916）查询按小时的流量统计信息**



Input: 

```
tccli mna GetFlowStatisticByName --cli-unfold-argument  \
    --DeviceName test0916 \
    --BeginTime 1757865600 \
    --EndTime 1758544927 \
    --Type 1 \
    --TimeGranularity 1
```

Output: 
```
{
    "Response": {
        "AvgValue": 51145200,
        "MaxValue": 51145200,
        "NetDetails": [
            {
                "Current": 51145200,
                "Time": "1758024000"
            }
        ],
        "RequestId": "3dc9c965-862b-46ea-b80a-0caf4368d0ba",
        "TotalValue": 51145200
    }
}
```

