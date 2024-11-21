**Example 1: 接收客户侧的用户已授权的号码**

接收客户侧的用户已授权的号码

Input: 

```
tccli trp AuthorizedTransfer --cli-unfold-argument  \
    --BusinessSecurityData.IsAuthorized 0 \
    --BusinessSecurityData.EncryptMethod 0 \
    --BusinessSecurityData.EncryptMode 0 \
    --BusinessSecurityData.PaddingType 0 \
    --BusinessSecurityData.EncryptData MjAyNDEwMjIxMTI5NTI4MjY=
```

Output: 
```
{
    "Response": {
        "Data": {
            "Code": 0,
            "Message": "操作成功",
            "Value": "说明"
        },
        "RequestId": "eaa3ccac-d2f5-4df0-a8b3-7b51324e9283"
    }
}
```

