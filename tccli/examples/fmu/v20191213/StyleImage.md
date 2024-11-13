**Example 1: 调用成功示例**



Input: 

```
tccli fmu StyleImage --cli-unfold-argument  \
    --Image /9j/4AAQSkZJRgABAQAAAQABAAD/4gIo...lftXF/DjFZNXoSP5V2U0HMt/1FQf/Z \
    --Url https://liudehua-9527.cos.ap-guangzhou.myqcloud.com/input.jpeg \
    --FilterDegree 1 \
    --FilterType 1 \
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

**Example 2: 调用返回失败**



Input: 

```
tccli fmu StyleImage --cli-unfold-argument  \
    --Image /9j/4AAQSkZJRgABAQAAAQABAAD/4gIo...lftXF/DjFZNXoSP5V2U0HMt/1FQf/Z \
    --Url https://liudehua-9527.cos.ap-guangzhou.myqcloud.com/input.jpeg \
    --FilterDegree 1 \
    --FilterType 1 \
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

