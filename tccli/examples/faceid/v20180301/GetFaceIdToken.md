**Example 1: 获取 SDK 核验 Token成功示例**



Input: 

```
tccli faceid GetFaceIdToken --cli-unfold-argument  \
    --CompareLib BUSINESS \
    --IdCard 11204416541220243X \
    --Name 韦小宝
```

Output: 
```
{
    "Response": {
        "FaceIdToken": "42S41B31D-5974-4674-EABB-8FFF1EC99F819",
        "RequestId": "94b54cdf-d975-4718-b091-32f8d79d6397"
    }
}
```

**Example 2: 获取 SDK 核验 Token失败示例**



Input: 

```
tccli faceid GetFaceIdToken --cli-unfold-argument  \
    --CompareLib LOCAL \
    --IdCard 11204416541220243X \
    --Name 韦小宝 \
    --ImageBase64 /9j/4AAQSkZJRg.....s97n//2Q==
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation.ImageSizeTooLarge",
            "Message": "图片尺寸过大。"
        },
        "RequestId": "ae8fbee0-f20e-4651-896e-e21e80d3822a"
    }
}
```

