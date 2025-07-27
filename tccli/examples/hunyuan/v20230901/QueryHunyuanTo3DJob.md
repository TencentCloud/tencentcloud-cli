**Example 1: 任务完成**

任务完成

Input: 

```
tccli hunyuan QueryHunyuanTo3DJob --cli-unfold-argument  \
    --JobId 1286221236421533696
```

Output: 
```
{
    "Response": {
        "ErrorCode": "",
        "ErrorMessage": "",
        "RequestId": "6ea0ea36-ea27-4870-9b9b-6937f7cc7117",
        "ResultFile3Ds": [
            {
                "File3D": [
                    {
                        "Type": "GIF",
                        "Url": "https://cos.ap-guangzhou.tencentcos.cn/3d/output.gif"
                    },
                    {
                        "Type": "OBJ",
                        "Url": "https://cos.ap-guangzhou.tencentcos.cn/3d/output/2e56fc_0.zip"
                    }
                ]
            }
        ],
        "Status": "DONE"
    }
}
```

