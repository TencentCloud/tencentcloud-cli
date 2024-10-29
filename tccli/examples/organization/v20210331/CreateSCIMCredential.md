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
        "CredentialSecret": "YlBKbEhkYXI2cy9xOEFjSyj9sngcXTyzqPMSkQl_qJ7IVNQGJoQJ9tUerclttS7PAWiabsIxkbCx3f3gR0qOWEqKmIF5N1RGrMqHxl0KhBq-BLowGXx8fpOipLmzYKYtjiO7CCUdkJ5_7de2nTCGEeC2yIu9dmJ5gtKwYBmjPW4F22cnReLf-2VeI5PDvqjKkZTu_WJ5vvUBoGlZsprEKapgVKEDdmYL04rvc-3u1__zTRbjC8PtncjqLvCx-9JsSilTZsVwldFCUDWAlOfmpcbdT1DaV9W8Ule-yOrqS-NJUUnJ4HsUzW3cL2nYiNQ2s5xD_DS7n691G6nhwK6xzu0po8Wy12oHx9RIhZ48d9kI9SwCwlrHZ0yNx7G__dtWdurhce2owPGLdETPPJlcOtCKFiNoHOc5EZox3ZKEVqo2CUA=",
        "CredentialStatus": "Enabled",
        "CredentialType": "BearerToken",
        "ExpireTime": "2025-05-31 15:04:53",
        "RequestId": "b835edd6-8ac0-4e79-9b78-917d3faff9ed",
        "ZoneId": "z-vft38p2hq8tq"
    }
}
```

