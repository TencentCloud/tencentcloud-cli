**Example 1: 查询生3D专业版示例**



Input: 

```
tccli ai3d QueryHunyuanTo3DProJob --cli-unfold-argument  \
    --JobId 1357237233311637504
```

Output: 
```
{
    "Response": {
        "ErrorCode": "",
        "ErrorMessage": "",
        "RequestId": "e4de438f-acca-44f9-9f29-7df547c81680",
        "ResultFile3Ds": [
            {
                "PreviewImageUrl": "https://cos.ap-guangzhou.tencentcos.cn/xxx.png",
                "Type": "GLB",
                "Url": "https://cos.ap-guangzhou.tencentcos.cn/xxx.glb"
            }
        ],
        "Status": "DONE"
    }
}
```

