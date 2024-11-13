**Example 1: 调用返回失败**



Input: 

```
tccli ft SwapGenderPic --cli-unfold-argument  \
    --Image /9j/4AAQSkZJRgABAQAAAQABAAD/4gIo...lftXF/DjFZNXoSP5V2U0HMt/1FQf/Z \
    --GenderInfos.0.Gender 1 \
    --GenderInfos.0.FaceRect.X 10 \
    --GenderInfos.0.FaceRect.Y 10 \
    --GenderInfos.0.FaceRect.Width 20 \
    --GenderInfos.0.FaceRect.Height 20 \
    --RspImgType url
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameterValue.ParameterValueError",
            "Message": "参数字段或者值有误。"
        },
        "RequestId": "b68b7c3a-410d-4af1-b63c-97450683b09b"
    }
}
```

**Example 2: 调用返回成功**



Input: 

```
tccli ft SwapGenderPic --cli-unfold-argument  \
    --Image /9j/4AAQSkZJRgABAQAAAQABAAD/4gIo...lftXF/DjFZNXoSP5V2U0HMt/1FQf/Z \
    --GenderInfos.0.Gender 1 \
    --GenderInfos.0.FaceRect.X 10 \
    --GenderInfos.0.FaceRect.Y 10 \
    --GenderInfos.0.FaceRect.Width 20 \
    --GenderInfos.0.FaceRect.Height 20 \
    --RspImgType url
```

Output: 
```
{
    "Response": {
        "ResultImage": "",
        "ResultUrl": "https://liudehua-9527.cos.ap-guangzhou.myqcloud.com/result.jpeg?q-sign-algorithm=sha1&q-ak=AKID********EXAMPLE&q-sign-time=8888;9999&q-key-time=8888;9999&q-header-list=&q-url-param-list=&q-signature=7de87f7bf9cfd23df9da32f46661e7cf97a5603c",
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

