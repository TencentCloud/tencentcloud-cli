**Example 1: 查询生3D专业版示例**



Input: 

```
tccli ai3d QueryHunyuanTo3DProJob --cli-unfold-argument  \
    --JobId 1423225609617285120
```

Output: 
```
{
    "Response": {
        "ErrorCode": "",
        "ErrorMessage": "",
        "ResultCreditConsumed": 40,
        "ResultCreditDetails": "{\"FaceCount\":10,\"GenerateType-Normal\":20,\"Pbr\":10}",
        "ResultFile3Ds": [
            {
                "PreviewImageUrl": "https://cos.ap-guangzhou.tencentcos.cn/xxx.png",
                "Type": "OBJ",
                "Url": "https://cos.ap-guangzhou.tencentcos.cn/xxx.zip"
            }
        ],
        "Status": "DONE",
        "RequestId": "8c73c29c-f871-470e-87ca-69219c82b550"
    }
}
```

