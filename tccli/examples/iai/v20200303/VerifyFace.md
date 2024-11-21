**Example 1: 人脸验证接口**

判断图片中的人和 PersonId 对应的人是否为同一人。

Input: 

```
tccli iai VerifyFace --cli-unfold-argument  \
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

