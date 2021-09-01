**Example 1: 人脸验证接口**



Input: 

```
tccli iai VerifyPerson --cli-unfold-argument  \
    --Url http://test.image.myqcloud.com/testA.jpg \
    --PersonId 11111111
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

