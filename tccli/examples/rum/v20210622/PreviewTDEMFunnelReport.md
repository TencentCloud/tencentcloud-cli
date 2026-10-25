**Example 1: 示例**



Input: 

```
tccli rum PreviewTDEMFunnelReport --cli-unfold-argument  \
    --AppId 1****7 \
    --StartTime 1718294400000 \
    --EndTime 1718380800000 \
    --Steps [{"StepName":"首页","PagePattern":"/","PageMatchMode":"exact","ActionType":"page_view"},{"StepName":"结算页","PagePattern":"/checkout","PageMatchMode":"prefix","ActionType":""}]
```

Output: 
```
{
    "Response": {
        "Result": "{\"FunnelId\": \"\", \"FunnelName\": \"\", \"Summary\": {\"TotalSessions\": 1000, \"ConversionRatio\": 0.5}, \"Steps\": [], \"Chart\": []}",
        "ErrorMsg": "",
        "RequestId": "c3ede0ff-9a91-4312-ac09-b2d8f7c597c7"
    }
}
```

