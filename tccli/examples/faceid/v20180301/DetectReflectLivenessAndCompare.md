**Example 1: 比对成功**



Input: 

```
tccli faceid DetectReflectLivenessAndCompare --cli-unfold-argument  \
    --ImageMd5 d41d8cd98f00b204e9800998ecf8427e \
    --LiveDataUrl https://faceid-resource-sg-1254418846.cos.ap-singapore.myqcloud.com/faceid%2FApplyWebVerificationToken%2F1300268875%2F20b11b59-572d-406d-8d94-e6e05782134c \
    --ImageUrl https://faceid-resource-sg-1254418846.cos.ap-singapore.myqcloud.com/faceid%2FApplyWebVerificationToken%2F1300268875%2F20b11b59-572d-406d-8d94-e6e05782134c \
    --LiveDataMd5 d41d8cd98f00b204e9800998ecf8427e
```

Output: 
```
{
    "Response": {
        "BestFrameUrl": "https://faceid-resource-sg-1254418846.cos.ap-singapore.myqcloud.com/faceid%2FApplyWebVerificationToken%2F1300268875%2F20b11b59-572d-406d-8d94-e6e05782134c",
        "Description": "Success",
        "BestFrameMd5": "d41d8cd98f00b204e9800998ecf8427e",
        "RequestId": "00577fa0-9d11-459e-a455-fc202ecd65bc",
        "Sim": 96.3,
        "Result": "Success"
    }
}
```

