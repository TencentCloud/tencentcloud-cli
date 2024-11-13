**Example 1: 调用返回失败**



Input: 

```
tccli fmu TryLipstickPic --cli-unfold-argument  \
    --Image /9j/4AAQSkZJRgABAQAAAQABAAD/4gIo...lftXF/DjFZNXoSP5V2U0HMt/1FQf/Z \
    --LipColorInfos.0.RGBA.R 220 \
    --LipColorInfos.0.RGBA.G 2 \
    --LipColorInfos.0.RGBA.B 44 \
    --LipColorInfos.0.RGBA.A 50 \
    --LipColorInfos.0.ModelAlpha 50 \
    --RspImgType base64
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

**Example 2: 调用返回成功（使用RGBA指定唇色）**



Input: 

```
tccli fmu TryLipstickPic --cli-unfold-argument  \
    --Image /9j/4AAQSkZJRgABAQAAAQABAAD/4gIo...lftXF/DjFZNXoSP5V2U0HMt/1FQf/Z \
    --LipColorInfos.0.RGBA.R 220 \
    --LipColorInfos.0.RGBA.G 2 \
    --LipColorInfos.0.RGBA.B 44 \
    --LipColorInfos.0.RGBA.A 50 \
    --LipColorInfos.0.ModelAlpha 50 \
    --RspImgType base64
```

Output: 
```
{
    "Response": {
        "ResultImage": "/9j/4AAQSkZJRgABAQAAAQABAAD/4gIo...lftXF/DjFZNXoSP5V2U0HMt/1FQf/Z",
        "ResultUrl": "",
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

**Example 3: 调用返回成功（使用Lut素材modelid指定唇色）**



Input: 

```
tccli fmu TryLipstickPic --cli-unfold-argument  \
    --Image /9j/4AAQSkZJRgABAQAAAQABAAD/4gIo...lftXF/DjFZNXoSP5V2U0HMt/1FQf/Z \
    --LipColorInfos.0.ModelId mo_0_1622620141111_1259088111_1 \
    --RspImgType base64
```

Output: 
```
{
    "Response": {
        "ResultImage": "/9j/4AAQSkZJRgABAQAAAQABAAD/4gIo...lftXF/DjFZNXoSP5V2U0HMt/1FQf/Z",
        "ResultUrl": "",
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

**Example 4: 调用返回成功（图片有多张脸时指定人脸框）**

您可以通过 [人脸检测与分析](https://cloud.tencent.com/document/api/867/32800) 接口获取图片的人脸框位置信息。

Input: 

```
tccli fmu TryLipstickPic --cli-unfold-argument  \
    --Image /9j/4AAQSkZJRgABAQAAAQABAAD/4gIo...lftXF/DjFZNXoSP5V2U0HMt/1FQf/Z \
    --LipColorInfos.0.ModelId mo_0_1622620141111_1259088111_1 \
    --LipColorInfos.1.ModelId mo_0_1622620141238_1259088111_2 \
    --RspImgType base64
```

Output: 
```
{
    "Response": {
        "ResultImage": "/9j/4AAQSkZJRgABAQAAAQABAAD/4gIo...lftXF/DjFZNXoSP5V2U0HMt/1FQf/Z",
        "ResultUrl": "",
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

