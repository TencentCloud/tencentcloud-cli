**Example 1: 接收客户侧的用户已授权的号码**

接收客户侧的用户已授权的号码

Input: 

```
tccli trp AuthorizedTransfer --cli-unfold-argument  \
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

