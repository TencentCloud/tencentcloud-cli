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
    --Agent.AppId yDwftUUwurrf2UEzGFaDwrXLPJYGIA7E \
    --Agent.ProxyOperator.OpenId eddisonchen \
    --Agent.ProxyAppId yDwFoUUyw3z5lUEi3kYK8mfxkDTjdxQH \
    --Agent.ProxyOrganizationId yDxj5UUpt8vrbUy0fKyKRq5QqcP9pOg1 \
    --FlowId yDwh0UUfy1xxbUEq8gZ2w0AhzSoRFnQv \
    --Operator.OpenId eddisonchen
```

Output: 
```
{
    "Response": {
        "PdfVerifyResults": [
            {
                "CertNotAfter": 1716370504000,
                "CertNotBefore": 1684748104000,
                "CertSn": "59c409xxxxxxxxxxxxxxxxxxxxxxdf5c36cf",
                "ComponentHeight": 119,
                "ComponentPage": 1,
                "ComponentPosX": 210.5,
                "ComponentPosY": 221,
                "ComponentWidth": 119,
                "SignAlgorithm": "SHA1withRSA",
                "SignPlatform": "腾讯电子签",
                "SignTime": 1690278683000,
                "SignType": 0,
                "SignerName": "XXXXXXXXXX测试有限公司",
                "VerifyResult": 0
            },
            {
                "CertNotAfter": 1716370504000,
                "CertNotBefore": 1684748104000,
                "CertSn": "59c409xxxxxxxxxxxxxxxxxxxxxxdf5c36cf",
                "ComponentHeight": 13.70001220703125,
                "ComponentPage": 1,
                "ComponentPosX": 210.5,
                "ComponentPosY": 343.1499938964844,
                "ComponentWidth": 119,
                "SignAlgorithm": "SHA1withRSA",
                "SignPlatform": "腾讯电子签",
                "SignTime": 1690277903000,
                "SignType": 0,
                "SignerName": "XXXXXXXXXX测试有限公司",
                "VerifyResult": 0
            }
        ],
        "RequestId": "8a8ba2e4-XXXX-XXXX-8dfcf4eb9bb3",
        "VerifyResult": 1
    }
}
```

