**Example 1: 调用返回失败**



Input: 

```
tccli facefusion FaceFusion --cli-unfold-argument  \
    --ProjectId 100646 \
    --ModelId qc_100646_154021_9 \
    --Image base64 \
    --RspImgType url
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation.FuseDetectNoFace",
            "Message": "未检测到人脸."
        },
        "RequestId": "8ae581fd-c25f-4a63-83b3-d9fcd97230c8"
    }
}
```

**Example 2: 调用返回成功**



Input: 

```
tccli facefusion FaceFusion --cli-unfold-argument  \
    --ProjectId 100646 \
    --ModelId qc_100646_154021_9 \
    --Image base64 \
    --RspImgType url
```

Output: 
```
{
    "Response": {
        "Image": "https://xxxx.jpg",
        "RequestId": "66676130-5588-4cdb-a81e-8bd3c99cea1f",
        "ReviewResultSet": [
            {
                "Category": "Politics",
                "Code": "0",
                "CodeDescription": "OK",
                "Suggestion": "PASS",
                "Confidence": 30,
                "DetailSet": [
                    {
                        "Field": "",
                        "Label": "",
                        "Confidence": 30,
                        "Suggestion": "PASS"
                    }
                ]
            }
        ]
    }
}
```

