**Example 1: 调用返回失败**



Input: 

```
tccli fmu CreateModel --cli-unfold-argument  \
    --LUTFile /9j/4AAQSkZJRgABAQAAAQABAAD/4gIo...lftXF/DjFZNXoSP5V2U0HMt/1FQf/Z \
    --Description 红色
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameterValue.LutImageInvalid",
            "Message": "图片不合法，必须是512*512的PNG图片。"
        },
        "RequestId": "615c23aa-8877-4a10-b01b-50a3d346050f"
    }
}
```

**Example 2: 调用返回成功**



Input: 

```
tccli fmu CreateModel --cli-unfold-argument  \
    --LUTFile /9j/4AAQSkZJRgABAQAAAQABAAD/4gIo...lftXF/DjFZNXoSP5V2U0HMt/1FQf/Z \
    --Description 红色
```

Output: 
```
{
    "Response": {
        "ModelId": "mo_0_1731389015111_1259088222_3",
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

