**Example 1: 查看个人自动签状态**

查看个人自动签状态, 同时也会返回自动签license类型，如果是 0 类型，则同时会返回开始和过期时间。

Input: 

```
tccli ess DescribeUserAutoSignStatus --cli-unfold-argument  \
    --Operator.ClientIp 1.2.3.4 \
    --Operator.UserId yDRCLUUgygq2xu********Ewg0vjoimj \
    --UserInfo.Name 典子谦 \
    --UserInfo.IdCardType ID_CARD \
    --UserInfo.IdCardNumber 620000198802020000 \
    --SceneKey E_PRESCRIPTION_AUTO_SIGN
```

Output: 
```
{
    "Response": {
        "IsOpen": true,
        "LicenseFrom": 1684412179,
        "LicenseTo": 1715948179,
        "LicenseType": 0,
        "RequestId": "5beb5fxxxxx-a97c85196a3e"
    }
}
```

