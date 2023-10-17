**Example 1: 示例**

1.对流程合同yDwFdUUckpsveo27UEQPEVo14KnASuGI进行数字签名验证
2.流程合同yDwFdUUckpsveo27UEQPEVo14KnASuGI验证正常

Input: 

```
tccli ess VerifyPdf --cli-unfold-argument  \
    --Operator.UserId yDxVwUyKQWho8CUuO4zjEyQOAgwvr4Zy \
    --FlowId yDwFdUUckpsveo27UEQPEVo14KnASuGI
```

Output: 
```
{
    "Response": {
        "PdfVerifyResults": [
            {
                "CertNotAfter": 166300032000,
                "CertNotBefore": 16630002000,
                "CertSn": "166300032000",
                "ComponentHeight": 33.340026855469,
                "ComponentPage": 1,
                "ComponentPosX": 160,
                "ComponentPosY": 293.32995605469,
                "ComponentWidth": 100,
                "SignAlgorithm": "SHA1withRSA",
                "SignPlatform": "腾讯电子签",
                "SignTime": 1663304532000,
                "SignerName": "ESS@xxx二@41xxxxx6635@666744",
                "VerifyResult": 1
            },
            {
                "CertNotAfter": 1663304655000,
                "CertNotBefore": 1663304655000,
                "CertSn": "2b42298dcxxxxx7527eaa1017e254e8",
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
        "RequestId": "79900a28xxxxxx-4af8a90f7292",
        "VerifySerialNo": "16698630779",
        "VerifyResult": 1,
        "PdfResourceMd5": "8879F721C764ABC918FD862B748F691C"
    }
}
```

**Example 2: 对流程合同文件进行验签-验签失败（文件被篡改）**

1.对流程合同yDwFdUUckpsvet4jUEn0aFRxtu5TdalM进行数字签名验证
2.流程合同yDwFdUUckpsvet4jUEn0aFRxtu5TdalM的文件被篡改，验证失败

Input: 

```
tccli ess VerifyPdf --cli-unfold-argument  \
    --Operator.UserId yDxVwUyKQWho8CUuO4zjEyQOAgwvr4Zy \
    --FlowId yDwFdUUckpsvet4jUEn0aFRxtu5TdalM
```

Output: 
```
{
    "Response": {
        "PdfVerifyResults": [
            {
                "CertNotAfter": 16691000034000,
                "CertNotBefore": 163700034000,
                "CertSn": "5255f51cxxxxxx4d66f2a9eb8fb3d2bc1",
                "ComponentHeight": 43,
                "ComponentPage": 1,
                "ComponentPosX": 210.25,
                "ComponentPosY": 43,
                "ComponentWidth": 96.75,
                "SignAlgorithm": "SHA1withRSA",
                "SignPlatform": "腾讯电子签",
                "SignTime": 1663238861000,
                "SignerName": "深圳市腾讯计算机系统有限公司",
                "VerifyResult": 3
            },
            {
                "CertNotAfter": 166300032000,
                "CertNotBefore": 166300032000,
                "CertSn": "5255f51c7xxx82c4d66f2a9eb8fb3d2bc1",
                "ComponentHeight": 12,
                "ComponentPage": 1,
                "ComponentPosX": 223.64999389648,
                "ComponentPosY": 86,
                "ComponentWidth": 69.950012207031,
                "SignAlgorithm": "SHA1withRSA",
                "SignPlatform": "腾讯电子签",
                "SignTime": 1663238861000,
                "SignerName": "深圳xxxxx限公司",
                "VerifyResult": 3
            }
        ],
        "RequestId": "57151f15-2xxxxxx46418d4b72a",
        "VerifySerialNo": "16698630779",
        "VerifyResult": 3,
        "PdfResourceMd5": "49649219B8771ACB538D418810983716"
    }
}
```

