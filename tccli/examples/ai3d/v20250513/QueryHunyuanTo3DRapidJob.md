**Example 1: 查询任务调用示例**



Input: 

```
tccli ai3d QueryHunyuanTo3DRapidJob --cli-unfold-argument  \
    --JobId 1336255233494892544
```

Output: 
```
{
    "Response": {
        "ErrorCode": "",
        "ErrorMessage": "",
        "RequestId": "3020cd6c-4ad6-4df3-8560-c233f35d6221",
        "ResultFile3Ds": [
            {
                "PreviewImageUrl": "https://xxx.cos.ap-guangzhou.tencentcos.cn/xxx.png",
                "Type": "OBJ",
                "Url": "https:/xxx.cos.ap-guangzhou.tencentcos.cn/xxx.zip"
            }
        ],
        "Status": "DONE"
    }
}
```

