**Example 1: 获取Web核验服务结果信息**



Input: 

```
tccli faceid GetWebVerificationResultIntl --cli-unfold-argument  \
    --BizToken EE13636D-1985-42CA-BD61-73F4C8B687E6
```

Output: 
```
{
    "Response": {
        "ErrorCode": 0,
        "ErrorMsg": "Success",
        "RequestId": "a6e62364-60d4-4eb6-8908-da3ff3d601f8",
        "VerificationDetailList": [
            {
                "ErrorCode": 0,
                "ErrorMsg": "Success",
                "LivenessErrorCode": 0,
                "LivenessErrorMsg": "Success",
                "CompareErrorCode": 0,
                "CompareErrorMsg": "Success",
                "Similarity": 100,
                "ReqTimestamp": 1637291599353,
                "Seq": "7269e30e-c142-46ba-aa60-b5677bf69d24"
            }
        ],
        "BestFrameBase64": "BestFrameBase64string",
        "VideoBase64": "VideoBase64string"
    }
}
```

