**Example 1: 离线筛选包数据推送**

接收离线筛选包回执，用于效果统计和分析。

Input: 

```
tccli trp ReportBatchCallbackStatus --cli-unfold-argument  \
    --BusinessSecurityData.IsAuthorized 0 \
    --BusinessSecurityData.EncryptMethod 0 \
    --BusinessSecurityData.EncryptMode 0 \
    --BusinessSecurityData.PaddingType 0 \
    --BusinessSecurityData.EncryptData abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "Code": 0,
            "Message": "abc",
            "Value": "abc"
        },
        "RequestId": "abc"
    }
}
```

