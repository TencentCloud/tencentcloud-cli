**Example 1: 离线筛选包数据推送**

接收离线筛选包回执，用于效果统计和分析。

Input: 

```
tccli trp ReportBatchCallbackStatus --cli-unfold-argument  \
    --BusinessSecurityData.IsAuthorized 1 \
    --BusinessSecurityData.EncryptMethod 2 \
    --BusinessSecurityData.EncryptMode 1 \
    --BusinessSecurityData.PaddingType 1 \
    --BusinessSecurityData.EncryptData hQDFcd2Gt1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Code": 0,
            "Message": "操作成功",
            "Value": "用户信息已获取"
        },
        "RequestId": "eaa3ccac-d2f5-4df0-a8b3-7b51324e9283"
    }
}
```

