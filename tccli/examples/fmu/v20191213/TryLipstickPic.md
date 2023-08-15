**Example 1: 调用返回成功（使用RGBA指定唇色）**



Input: 

```
tccli fmu TryLipstickPic --cli-unfold-argument  \
    --Image xxxxx \
    --LipColorInfos.0.RGBA.R 200 \
    --LipColorInfos.0.RGBA.G 0 \
    --LipColorInfos.0.RGBA.B 0 \
    --LipColorInfos.0.RGBA.A 50
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

**Example 2: 调用返回成功（使用Lut素材modelid指定唇色）**



Input: 

```
tccli fmu TryLipstickPic --cli-unfold-argument  \
    --Image xxxxx \
    --LipColorInfos.0.ModelId xxx
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

**Example 3: 调用返回成功（图片有多张脸时指定人脸框）**

您可以通过 [人脸检测与分析](https://cloud.tencent.com/document/api/867/32800) 接口获取图片的人脸框位置信息。

Input: 

```
tccli fmu TryLipstickPic --cli-unfold-argument  \
    --Image xxxxx \
    --LipColorInfos.0.ModelId xxx \
    --LipColorInfos.0.FaceRect.X 整型 \
    --LipColorInfos.0.FaceRect.Y 整型 \
    --LipColorInfos.0.FaceRect.Width 整型 \
    --LipColorInfos.0.FaceRect.Height 整型 \
    --LipColorInfos.1.ModelId xxx \
    --LipColorInfos.1.FaceRect.X 整型 \
    --LipColorInfos.1.FaceRect.Y 整型 \
    --LipColorInfos.1.FaceRect.Width 整型 \
    --LipColorInfos.1.FaceRect.Height 整型
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

**Example 4: 调用返回失败**



Input: 

```
tccli fmu TryLipstickPic --cli-unfold-argument  \
    --Image xxxxx \
    --LipColorInfos.0.RGBA.R 200 \
    --LipColorInfos.0.RGBA.G 0 \
    --LipColorInfos.0.RGBA.B 0 \
    --LipColorInfos.0.RGBA.A 50
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

