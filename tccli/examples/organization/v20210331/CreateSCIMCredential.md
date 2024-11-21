**Example 1: 创建SCIM密钥**

创建SCIM密钥

Input: 

```
tccli organization CreateSCIMCredential --cli-unfold-argument  \
    --ZoneId z-vft38p2hq8tq
```

Output: 
```
{
    "Response": {
        "CreateTime": "2024-05-31 15:04:53",
        "CredentialId": "scimcred-un1tgbnt0s9j",
        "CredentialSecret": "YlBKbEhkYXI2cy9xOEFjSyj**************PJlcOtCKFiNoHOc5EZox3ZKEVqo2CUA=",
        "CredentialStatus": "Enabled",
        "CredentialType": "BearerToken",
        "ExpireTime": "2025-05-31 15:04:53",
        "RequestId": "b835edd6-8ac0-4e79-9b78-917d3faff9ed",
        "ZoneId": "z-vft38p2hq8tq"
    }
}
```

