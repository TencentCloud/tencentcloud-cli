**Example 1: 调用返回失败**



Input: 

```
tccli ft ChangeAgePic --cli-unfold-argument  \
    --Image xxxxx \
    --AgeInfos.0.Age 10 \
    --AgeInfos.0.FaceRect.X 10 \
    --AgeInfos.0.FaceRect.Y 10 \
    --AgeInfos.0.FaceRect.Width 20 \
    --AgeInfos.0.FaceRect.Height 20
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
tccli ft ChangeAgePic --cli-unfold-argument  \
    --Image xxxxx \
    --AgeInfos.0.Age 10 \
    --AgeInfos.0.FaceRect.X 10 \
    --AgeInfos.0.FaceRect.Y 10 \
    --AgeInfos.0.FaceRect.Width 20 \
    --AgeInfos.0.FaceRect.Height 20
```

Output: 
```
{
    "Response": {
        "ResultImage": "base64编码的图片",
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

