**Example 1: 示例-验证不通过**

示例-验证不通过

Input: 

```
tccli essbasic ChannelVerifyPdf --cli-unfold-argument  \
    --Operator.OpenId testxxxx_test1 \
    --FlowId yDRvzUUgxxxxygxxxx4zjEuYdDnsxeT \
    --Agent.ProxyOperator.OpenId test1_xxxxx_test1 \
    --Agent.AppId 7f3497f01xxxa35e0984a9657b0ec \
    --Agent.ProxyOrganizationOpenId test1_cxxxx_organization1
```

Output: 
```
{
    "Response": {
        "PdfVerifyResults": [],
        "RequestId": "8709904xxxxxx7-d1bc7420345f",
        "VerifyResult": 4
    }
}
```

**Example 2: 示例-验证通过**

示例-验证通过

Input: 

```
tccli essbasic ChannelVerifyPdf --cli-unfold-argument  \
    --Operator.OpenId testxxxx_test1 \
    --FlowId yDRvzUUgxxxxygxxxx4zjEuYdDnsxeT \
    --Agent.ProxyOperator.OpenId test1_clara_test1 \
    --Agent.AppId 7f3497f01xxxa35e0984a9657b0ec \
    --Agent.ProxyOrganizationOpenId test1_cxxxx_organization1
```

Output: 
```
{
    "Response": {
        "PdfVerifyResults": [
            {
                "CertNotAfter": 0,
                "CertNotBefore": 0,
                "CertSn": "",
                "ComponentHeight": 0,
                "ComponentPage": 0,
                "ComponentPosX": 0,
                "ComponentPosY": 0,
                "ComponentWidth": 0,
                "SignAlgorithm": "",
                "SignPlatform": "",
                "SignTime": 0,
                "SignType": 0,
                "SignerName": "",
                "VerifyResult": 0
            },
            {
                "CertNotAfter": 0,
                "CertNotBefore": 0,
                "CertSn": "",
                "ComponentHeight": 0,
                "ComponentPage": 0,
                "ComponentPosX": 0,
                "ComponentPosY": 0,
                "ComponentWidth": 0,
                "SignAlgorithm": "",
                "SignPlatform": "",
                "SignTime": 0,
                "SignType": 0,
                "SignerName": "",
                "VerifyResult": 0
            },
            {
                "CertNotAfter": 0,
                "CertNotBefore": 0,
                "CertSn": "",
                "ComponentHeight": 0,
                "ComponentPage": 0,
                "ComponentPosX": 0,
                "ComponentPosY": 0,
                "ComponentWidth": 0,
                "SignAlgorithm": "",
                "SignPlatform": "",
                "SignTime": 0,
                "SignType": 0,
                "SignerName": "",
                "VerifyResult": 0
            },
            {
                "CertNotAfter": 1646376026000,
                "CertNotBefore": 1646289626000,
                "CertSn": "1912050077215241",
                "ComponentHeight": 39.999969482422,
                "ComponentPage": 3,
                "ComponentPosX": 327.10998535156,
                "ComponentPosY": 321.78002929688,
                "ComponentWidth": 62.780029296875,
                "SignAlgorithm": "SHA1withRSA",
                "SignPlatform": "腾讯电子签",
                "SignTime": 1646289626000,
                "SignType": 0,
                "SignerName": "程英",
                "VerifyResult": 0
            },
            {
                "CertNotAfter": 1646376026000,
                "CertNotBefore": 1646289626000,
                "CertSn": "1912050077215241",
                "ComponentHeight": 12,
                "ComponentPage": 3,
                "ComponentPosX": 343.5299987793,
                "ComponentPosY": 404.7799987793,
                "ComponentWidth": 69.940002441406,
                "SignAlgorithm": "SHA1withRSA",
                "SignPlatform": "腾讯电子签",
                "SignTime": 1646289626000,
                "SignType": 0,
                "SignerName": "程英",
                "VerifyResult": 0
            },
            {
                "CertNotAfter": 1778601599000,
                "CertNotBefore": 1620835200000,
                "CertSn": "4c5a00000000000001839b86",
                "ComponentHeight": 0,
                "ComponentPage": 1,
                "ComponentPosX": 0,
                "ComponentPosY": 842,
                "ComponentWidth": 0,
                "SignAlgorithm": "SHA1withRSA",
                "SignPlatform": "腾讯电子签",
                "SignTime": 1646289627000,
                "SignType": 1,
                "SignerName": "深圳xxxx公司",
                "VerifyResult": 0
            }
        ],
        "RequestId": "9c683673-axxx2-648f67d46fad",
        "VerifyResult": 1
    }
}
```

