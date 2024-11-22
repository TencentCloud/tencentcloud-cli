**Example 1: 人脸静态活体检测（高精度版）成功示例**



Input: 

```
tccli iai DetectLiveFaceAccurate --cli-unfold-argument  \
    --Url http://test.image.myqcloud.com/testA.jpg
```

Output: 
```
{
    "Response": {
        "Score": 99,
        "FaceModelVersion": "3.0",
        "RequestId": "048a5eb3-f7a9-4c1f-a982-00e90b6b892c"
    }
}
```

**Example 2: 人脸静态活体检测（高精度版）失败示例**



Input: 

```
tccli iai DetectLiveFaceAccurate --cli-unfold-argument  \
    --Url http://test.image.myqcloud.com/testB.jpg
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation.ImageDecodeFailed",
            "Message": "图片解码失败。"
        },
        "RequestId": "0e77ad29-ad65-4901-9efc-b49a6e0a357b"
    }
}
```

