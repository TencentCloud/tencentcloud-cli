**Example 1: 人脸验证成功示例**



Input: 

```
tccli iai VerifyPerson --cli-unfold-argument  \
    --Url http://test.image.myqcloud.com/testA.jpg \
    --PersonId 1001
```

Output: 
```
{
    "Response": {
        "Score": 100,
        "IsMatch": true,
        "FaceModelVersion": "3.0",
        "RequestId": "a8eb4545-a154-4f86-9510-57a8be9cae0c"
    }
}
```

**Example 2: 人脸验证失败示例**



Input: 

```
tccli iai VerifyPerson --cli-unfold-argument  \
    --Url http://test.image.myqcloud.com/testB.jpg \
    --PersonId 1001
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

