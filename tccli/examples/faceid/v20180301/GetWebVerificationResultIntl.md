**Example 1: 获取Web核验服务结果信息**



Input: 

```
tccli faceid GetWebVerificationResultIntl --cli-unfold-argument  \
    --BizToken 4A7E7CE1-834C-4016-84DB-23823024233F
```

Output: 
```
{
    "Response": {
        "BestFrameBase64": "/9j/4AAQSkZJRgABAQAAA**",
        "ErrorCode": 0,
        "ErrorMsg": "Success, tap next to continue",
        "Extra": null,
        "OCRResult": null,
        "RequestId": "e7ad0f19-0c3e-402f-9fb0-720dd7ed0d99",
        "VerificationDetailList": [
            {
                "CompareErrorCode": null,
                "CompareErrorMsg": null,
                "ErrorCode": 0,
                "ErrorMsg": "Success, tap next to continue",
                "LivenessErrorCode": 0,
                "LivenessErrorMsg": "Success, tap next to continue",
                "LivenessInfoTag": null,
                "ReqTimestamp": 1789473304325,
                "Seq": "11a370d4-9a16-49c8-b1bb-74ad89ac6965",
                "Similarity": 0
            }
        ],
        "VideoBase64": "AAAAIGZ0eXBpc29tAAACAG**"
    }
}
```

