**Example 1: 批量上报设备消息**

成功响应

Input: 

```
tccli weilingwith BatchReportAppMessage --cli-unfold-argument  \
    --WorkspaceId 1016 \
    --ApplicationToken baSTzPx0vZ6LPuv2EifNa5CqRBj9hoY0 \
    --ReportSet.0.WorkspaceId 1016 \
    --ReportSet.0.Profile.AppType security \
    --ReportSet.0.ReportTs 1 \
    --ReportSet.0.Properties x-json:{"executeId": "RX_TASK"}
```

Output: 
```
{
    "Response": {
        "RequestId": "b3cac805-15a2-4766-9ef6-77929e509db9",
        "Result": {
            "Commit": 1,
            "SpanMap": [
                {
                    "ReportId": "0000000000000000",
                    "ReportStatus": 1
                }
            ],
            "TotalElements": 1
        }
    }
}
```

