**Example 1: 批量删除示例**



Input: 

```
tccli trtc BatchDeleteTRTCVoicePrint --cli-unfold-argument  \
    --VoicePrintIds 19dbb1d12cd_9610feccb7dc4548910724f3f78a2d9d \
    --SdkAppId 1400123456
```

Output: 
```
{
    "Response": {
        "FailCount": 1,
        "Message": "batch delete completed: 1 succeeded, 1 failed",
        "Results": [
            {
                "ErrorCode": "FailedOperation.VoiceprintNotFound",
                "ErrorMessage": "voiceprint not found",
                "VoicePrintId": "19dbb1d12cd_9610feccb7dc4548910724f3f78a2d9d"
            }
        ],
        "SuccessCount": 1,
        "RequestId": "37584dec-d405-4ed4-8af8-61e21db06ac6"
    }
}
```

