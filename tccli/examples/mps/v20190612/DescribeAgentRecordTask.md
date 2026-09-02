**Example 1: 示例**



Input: 

```
tccli mps DescribeAgentRecordTask --cli-unfold-argument  \
    --TaskId 24000192-MllmVideoTest-9baf86edd37b1491037414981e556bf0
```

Output: 
```
{
    "Response": {
        "RecordUrls": [
            "https://***********-live-record-task-**********.cos.ap-guangzhou.myqcloud.com/record-only/24000192-MllmVideoTest-7fedc0fb7c4fc718fd9792ca8e04e80f-2026-07-15-12-04-29.mp4"
        ],
        "Status": "RUNNING",
        "RequestId": "092b9f39-6bbd-4d34-b9aa-b5693f639edf"
    }
}
```

