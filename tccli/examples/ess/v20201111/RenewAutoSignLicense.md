**Example 1: 续期医疗个人自动签许可**

给医疗个人自动签许可续期，续期成功返回追加一年后的有效期。

Input: 

```
tccli ess RenewAutoSignLicense --cli-unfold-argument  \
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
        "LicenseTo": 1715948179,
        "RequestId": "5beb5fxxxxx-a97c85196a3e"
    }
}
```

