**Example 1: 输入原文进行签名**



Input: 

```
tccli ess CreateDigitalDataSign --cli-unfold-argument  \
    --Operator.UserId yDw**********************Rl77mox \
    --PlainText 测试abc
```

Output: 
```
{
    "Response": {
        "Certificate": {
            "CommonName": "ESS*******************782683",
            "IssuerCommonName": "NMGSCA TEST RSA OCA1",
            "NotAfter": 1800385201,
            "NotBefore": 1768849201,
            "SerialNumber": "220***********ab"
        },
        "SignAlgorithm": "RSA",
        "SignTimestamp": "MIIQHgYJKoZIhvNdoQ7niijSz8RtbRgul09Kcac9xiHwaU0SxCmU4pzu8IY0zL3Sk3qULParIU=",
        "SignValue": "MIAGCSqGSIb3DQEHAqCAMIACAQGSIb3DQEHATAcBgkqhkiG9w0B",
        "RequestId": "fe8f8be8-b5b6-4ca1-bc04-979139f95ebc"
    }
}
```

