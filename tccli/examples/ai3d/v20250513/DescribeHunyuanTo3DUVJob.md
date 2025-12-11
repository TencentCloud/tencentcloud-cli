**Example 1: 查询UV展示任务示例**



Input: 

```
tccli ai3d DescribeHunyuanTo3DUVJob --cli-unfold-argument  \
    --JobId 1315932989749215232
```

Output: 
```
{
    "Response": {
        "ErrorCode": "",
        "ErrorMessage": "",
        "RequestId": "5fec6e4d-9780-4372-815a-15490cb2ed5a",
        "ResultFile3Ds": [
            {
                "Type": "OBJ",
                "Url": "https://cos.ap-guangzhou.tencentcos.cn/xxx.obj"
            },
            {
                "Type": "FBX",
                "Url": "https://cos.ap-guangzhou.tencentcos.cn/xxx.fbx"
            },
            {
                "Type": "IMAGE",
                "Url": "https://cos.ap-guangzhou.tencentcos.cn/xxx.png"
            }
        ],
        "Status": "DONE"
    }
}
```

