**Example 1: 调用请求示例**



Input: 

```
tccli ai3d QueryHunyuanTo3DJob --cli-unfold-argument  \
    --JobId 1315932989749215232
```

Output: 
```
{
    "Response": {
        "ErrorCode": "",
        "ErrorMessage": "",
        "RequestId": "cfbcde8e-dc35-47ec-adda-0fa6d5db1dd2",
        "ResultFile3Ds": [
            {
                "Type": "STL",
                "Url": "https://xxx.cos.ap-guangzhou.tencentcos.cn/xxx.stl",
                "PreviewImageUrl": "https://xxx.cos.ap-guangzhou.tencentcos.cn/xxx.png"
            }
        ],
        "Status": "DONE"
    }
}
```

