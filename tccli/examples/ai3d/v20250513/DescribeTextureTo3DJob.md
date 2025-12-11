**Example 1: 任务完成**

任务成功完成

Input: 

```
tccli ai3d DescribeTextureTo3DJob --cli-unfold-argument  \
    --JobId 1318771057486315520
```

Output: 
```
{
    "Response": {
        "ErrorCode": "",
        "ErrorMessage": "",
        "RequestId": "fd7fc2dd-8fcf-4c52-839a-8f7e729e434d",
        "ResultFile3Ds": [
            {
                "Type": "TEXTURE_IMAGE",
                "Url": "https://***.cos.ap-guangzhou.myqcloud.com/image.jpg/***.png"
            },
            {
                "Type": "MTL",
                "Url": "https://***.cos.ap-guangzhou.myqcloud.com/image.jpg/***.mtl"
            },
            {
                "Type": "ZIP",
                "Url": "https://***.cos.ap-guangzhou.myqcloud.com/image.jpg/***.zip"
            },
            {
                "Type": "OBJ",
                "Url": "https://***.cos.ap-guangzhou.myqcloud.com/image.jpg/***.obj"
            },
            {
                "Type": "GLB",
                "Url": "https://***.cos.ap-guangzhou.myqcloud.com/image.jpg/***.glb"
            },
            {
                "Type": "IMAGE",
                "Url": "https://***.cos.ap-guangzhou.myqcloud.com/image.jpg/***.png"
            }
        ],
        "Status": "DONE"
    }
}
```

