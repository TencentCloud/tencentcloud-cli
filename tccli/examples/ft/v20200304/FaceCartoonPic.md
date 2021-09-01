**Example 1: 调用返回失败**



Input: 

```
tccli ft FaceCartoonPic --cli-unfold-argument  \
    --Image xxxxx \
    --Url xxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "b68b7c3a-410d-4af1-b63c-97450683b09b"
    }
}
```

**Example 2: 调用返回成功**



Input: 

```
tccli ft FaceCartoonPic --cli-unfold-argument  \
    --Image xxxxx \
    --Url xxxxx
```

Output: 
```
{
    "Response": {
        "ResultImage": "base64编码的图片",
        "ResultUrl": "",
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

