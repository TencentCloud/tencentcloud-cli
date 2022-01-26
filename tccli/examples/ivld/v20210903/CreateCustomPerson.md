**Example 1: 成功创建自定义人物**



Input: 

```
tccli ivld CreateCustomPerson --cli-unfold-argument  \
    --ImageURL https://test-251202813.cos.ap-guangzhou.myqcloud.com/%E6%B2%88%E8%85%BE.jpeg \
    --BasicInfo 测试基本信息 \
    --Name 测试姓名 \
    --CategoryId 11
```

Output: 
```
{
    "Response": {
        "ImageInfo": {
            "ErrorCode": "OK",
            "ErrorMsg": "OK",
            "ImageId": "image-Axgo3FYc-egMN",
            "ImageURL": "https://test-251202813.cos.ap-guangzhou.myqcloud.com/CustomImages/image-Axgo3FYc-egMN.jpeg"
        },
        "PersonId": "person-Axgo3FYc",
        "RequestId": "705f6aed-f46b-4f43-aeef-31167885d938"
    }
}
```

