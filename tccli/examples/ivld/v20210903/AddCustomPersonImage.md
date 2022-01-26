**Example 1: 新增自定义人物图片**



Input: 

```
tccli ivld AddCustomPersonImage --cli-unfold-argument  \
    --PersonId person-Axgo3FYc \
    --ImageURL https://test-251202813.cos.ap-guangzhou.myqcloud.com/%E6%B2%88%E8%85%BE.jpeg
```

Output: 
```
{
    "Response": {
        "ImageInfo": {
            "ErrorCode": "OK",
            "ErrorMsg": "OK",
            "ImageId": "image-Axgo3FYc-GOeV",
            "ImageURL": "https://test-251202813.cos.ap-guangzhou.myqcloud.com/CustomImages/image-Axgo3FYc-GOeV.jpeg"
        },
        "PersonId": "person-Axgo3FYc",
        "RequestId": "f7efda76-2d0d-487d-9e8c-4c198555cc1f"
    }
}
```

