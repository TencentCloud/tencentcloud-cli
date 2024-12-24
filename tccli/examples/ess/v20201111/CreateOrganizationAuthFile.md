**Example 1: 生成企业认证超管授权书**



Input: 

```
tccli ess CreateOrganizationAuthFile --cli-unfold-argument  \
    --Operator.UserId yDRt2UUgygqxyp9yUuO4zjEwqXwsIljA \
    --OrganizationCommonInfo.OrganizationName 典子签测试企业 \
    --OrganizationCommonInfo.UniformSocialCreditCode N26XXXXXX523 \
    --OrganizationCommonInfo.LegalName 鹅鹅子 \
    --OrganizationCommonInfo.LegalIdCardType  \
    --OrganizationCommonInfo.LegalIdCardNumber 110XXXXXX20 \
    --OrganizationCommonInfo.AdminName 鹅鹅子 \
    --OrganizationCommonInfo.AdminMobile 130XXXXX222 \
    --OrganizationCommonInfo.AdminIdCardType  \
    --OrganizationCommonInfo.AdminIdCardNumber 110XXXXXX2020 \
    --Type 0
```

Output: 
```
{
    "Response": {
        "FileUrl": "https://file.test.ess.tencent.cn/bresource/resource/resource/0/0.PDF?hkey=22c08eb99607114e98ae7397a78f7cdc393a2dd9863f9f7d2f68890fb3219769a075e4f8e9631cf756ec0f7f27af6532925007e4dbf226d9b61afa605493013d9c23f7ff0a1bf7f41658ee74b8c3f261d1bfdd3b9f184b780392a2323522175a6d80f469afe196e131bdd882200c95653994d7749a03b13ced4ba14af190898fb6463b19a80c78f22fe1ace31270ab77635505b55849fd7c89ee2b539faebe86",
        "RequestId": "s1734597439220564890"
    }
}
```

