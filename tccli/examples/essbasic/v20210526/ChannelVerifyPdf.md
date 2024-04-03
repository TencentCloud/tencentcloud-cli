**Example 1: 验证通过**

示例-验证通过

Input: 

```
tccli essbasic ChannelVerifyPdf --cli-unfold-argument  \
    --FlowId yDSLVUUckpo1c11xUxtOq8cvKy24by9M \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyAppId 
```

Output: 
```
{
    "Response": {
        "VerifyResult": 1,
        "PdfVerifyResults": [
            {
                "VerifyResult": 1,
                "SignPlatform": "腾讯电子签",
                "SignerName": "ESS@典子谦示例企业@382919",
                "SignTime": 1699252042000,
                "SignAlgorithm": "SHA1withRSA",
                "CertSn": "6c8e2911fadf70ea",
                "CertNotBefore": 1699006057000,
                "CertNotAfter": 1730542057000,
                "SignType": 0,
                "ComponentPosX": 361.0799865722656,
                "ComponentPosY": 481.6199951171875,
                "ComponentWidth": 119,
                "ComponentHeight": 13.70001220703125,
                "ComponentPage": 1
            },
            {
                "VerifyResult": 1,
                "SignPlatform": "腾讯电子签",
                "SignerName": "ESS@典子谦示例企业@382919",
                "SignTime": 1699252040000,
                "SignAlgorithm": "SHA1withRSA",
                "CertSn": "6c8e2911fadf70ea",
                "CertNotBefore": 1699006057000,
                "CertNotAfter": 1730542057000,
                "SignType": 0,
                "ComponentPosX": 361.0799865722656,
                "ComponentPosY": 359.45001220703125,
                "ComponentWidth": 119,
                "ComponentHeight": 119,
                "ComponentPage": 1
            },
            {
                "VerifyResult": 1,
                "SignPlatform": "腾讯电子签",
                "SignerName": "ESS@张三@37000019890303000X@808854",
                "SignTime": 1699252071000,
                "SignAlgorithm": "SHA1withRSA",
                "CertSn": "1000000000087449",
                "CertNotBefore": 1681301253000,
                "CertNotAfter": 1712837253000,
                "SignType": 0,
                "ComponentPosX": 193.55999755859375,
                "ComponentPosY": 43.90997314453125,
                "ComponentWidth": 86,
                "ComponentHeight": 43,
                "ComponentPage": 1
            },
            {
                "VerifyResult": 1,
                "SignPlatform": "腾讯电子签",
                "SignerName": "ESS@张三@37000019890303000X@808854",
                "SignTime": 1699252071000,
                "SignAlgorithm": "SHA1withRSA",
                "CertSn": "1000000000087449",
                "CertNotBefore": 1681301253000,
                "CertNotAfter": 1712837253000,
                "SignType": 0,
                "ComponentPosX": 177.05999755859375,
                "ComponentPosY": 90.25,
                "ComponentWidth": 119,
                "ComponentHeight": 13.70001220703125,
                "ComponentPage": 1
            }
        ],
        "VerifySerialNo": "16992543927198",
        "PdfResourceMd5": "708BE88A797843094A74FA10ABF08F01",
        "RequestId": "80c66dcb-fc07-48d4-8914-eb0171bbf1ac"
    }
}
```

**Example 2: 验证不通过**

验证不通过

Input: 

```
tccli essbasic ChannelVerifyPdf --cli-unfold-argument  \
    --FlowId yDSLWUUckposmpkvUyb9xvpEQeni94od \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyAppId 
```

Output: 
```
{
    "Response": {
        "VerifyResult": 4,
        "PdfVerifyResults": [],
        "VerifySerialNo": "16992543927198",
        "PdfResourceMd5": "708BE88A797843094A74FA10ABF08F01",
        "RequestId": "e5064ef6-4743-461a-9024-3120576f3f6b"
    }
}
```

