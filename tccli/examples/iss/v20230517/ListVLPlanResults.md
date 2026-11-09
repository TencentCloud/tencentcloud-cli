**Example 1: 成功示例**



Input: 

```
tccli iss ListVLPlanResults --cli-unfold-argument  \
    --Start 1790495635 \
    --End 1791791635 \
    --PageNumber 1 \
    --PageSize 1 \
    --AnalysisMode video
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "AnalysisMode": "video",
                "BilledFrameCount": 30,
                "ChannelId": "**********",
                "ChannelName": "*******",
                "Content": "{\"has_violation\":false,\"inspection_results\":[],\"task\":\"smoking_detection\"}",
                "CreatedAt": "2026-10-12 13:51:02",
                "SnapshotTimestamp": 0,
                "UpdatedAt": "2026-10-12 13:51:02",
                "VLPlanId": "VPa43**************************c86",
                "VLPlanName": "******",
                "VLPlanResultId": "eb63*****************************19d",
                "VLResultTimestamp": 1791784262,
                "VideoEndTimestamp": 1791784230,
                "VideoStartTimestamp": 1791784200
            }
        ],
        "TotalCount": 714,
        "RequestId": "bfc4d2b5-aeda-472f-a2e9-513e195a54ce"
    }
}
```

