**Example 1: 任务完成**

任务完成

Input: 

```
tccli ai3d DescribeProfileTo3DJob --cli-unfold-argument  \
    --JobId 1335073555113197568
```

Output: 
```
{
    "Response": {
        "ErrorCode": "",
        "ErrorMessage": "",
        "RequestId": "6636d5d9-5fe0-4928-be9d-0b8c9dc26847",
        "ResultFile3Ds": [
            {
                "Type": "POSTPROCESS_OBJ",
                "Url": "https://***.cos.ap-guangzhou.myqcloud.com/***.obj"
            },
            {
                "Type": "OBJ",
                "Url": "https://***.cos.ap-guangzhou.myqcloud.com/***.obj"
            },
            {
                "Type": "IMAGE",
                "Url": "https://***.cos.ap-guangzhou.myqcloud.com/***.png"
            },
            {
                "Type": "MTL",
                "Url": "https://***.cos.ap-guangzhou.myqcloud.com/***.mtl"
            },
            {
                "Type": "FBX",
                "Url": "https://***.cos.ap-guangzhou.myqcloud.com/***.fbx"
            }
        ],
        "Status": "DONE"
    }
}
```

