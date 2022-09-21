**Example 1: 示例**



Input: 

```
tccli ess VerifyPdf --cli-unfold-argument  \
    --Operator.UserId yDxoQUUgydjfn4yaUuO4zjEyd1h2hnnR \
    --FlowId yDRINUUgygs3yr3pUuO4zjEReF3rOOwb
```

Output: 
```
{
    "Response": {
        "PdfVerifyResults": [
            {
                "CertNotAfter": 1663275732000,
                "CertNotBefore": 1663275732000,
                "CertSn": "100000000712",
                "ComponentHeight": 33.340026855469,
                "ComponentPage": 1,
                "ComponentPosX": 160,
                "ComponentPosY": 293.32995605469,
                "ComponentWidth": 100,
                "SignAlgorithm": "SHA1withRSA",
                "SignPlatform": "腾讯电子签",
                "SignTime": 1663304532000,
                "SignerName": "ESS@xxx二@410403199607276635@666744",
                "VerifyResult": 1
            },
            {
                "CertNotAfter": 1663304655000,
                "CertNotBefore": 1663304655000,
                "CertSn": "2b42298dca7010443a377657527eaa1017e254e8",
                "ComponentHeight": 75.680023193359,
                "ComponentPage": 1,
                "ComponentPosX": 260,
                "ComponentPosY": 272.15997314453,
                "ComponentWidth": 100,
                "SignAlgorithm": "SHA1withRSA",
                "SignPlatform": "腾讯电子签",
                "SignTime": 1663304656000,
                "SignerName": "张x x",
                "VerifyResult": 1
            }
        ],
        "RequestId": "79900a28-edd7-4cdf-8ed8-4af8a90f7292",
        "VerifyResult": 1
    }
}
```

**Example 2: 示例1**



Input: 

```
tccli ess VerifyPdf --cli-unfold-argument  \
    --Operator.ProxyIp  \
    --Operator.ClientIp 8.8.8.8 \
    --Operator.UserId yDxoQUUgydjfn4yaUuO4zjEyd1h2hnnR \
    --Operator.Channel  \
    --Operator.OpenId  \
    --FlowId yDRIKUUgygs1jw2sUuO4zjExhs82XeuX
```

Output: 
```
{
    "Response": {
        "PdfVerifyResults": [
            {
                "CertNotAfter": 1669172034000,
                "CertNotBefore": 1637549634000,
                "CertSn": "5255f51c76425eb30882c4d66f2a9eb8fb3d2bc1",
                "ComponentHeight": 43,
                "ComponentPage": 1,
                "ComponentPosX": 210.25,
                "ComponentPosY": 43,
                "ComponentWidth": 96.75,
                "SignAlgorithm": "SHA1withRSA",
                "SignPlatform": "腾讯电子签",
                "SignTime": 1663238861000,
                "SignerName": "深圳市腾讯计算机系统有限公司",
                "VerifyResult": 1
            },
            {
                "CertNotAfter": 1669172034000,
                "CertNotBefore": 1637549634000,
                "CertSn": "5255f51c76425eb30882c4d66f2a9eb8fb3d2bc1",
                "ComponentHeight": 12,
                "ComponentPage": 1,
                "ComponentPosX": 223.64999389648,
                "ComponentPosY": 86,
                "ComponentWidth": 69.950012207031,
                "SignAlgorithm": "SHA1withRSA",
                "SignPlatform": "腾讯电子签",
                "SignTime": 1663238861000,
                "SignerName": "深圳市腾讯计算机系统有限公司",
                "VerifyResult": 1
            }
        ],
        "RequestId": "57151f15-2270-4f7e-9e17-346418d4b72a",
        "VerifyResult": 1
    }
}
```

