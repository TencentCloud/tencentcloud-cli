**Example 1: 生成企业电子印章**



Input: 

```
tccli essbasic GenerateOrganizationSeal --cli-unfold-argument  \
    --Caller.ApplicationId asbbdf9c2a7bdcb88811f4d0200fee3d \
    --Caller.SubOrganizationId  \
    --Caller.OperatorId  \
    --SealName 印章名称 \
    --SealType OFFICIAL \
    --SealHorizontalText 腾讯电子印章 \
    --SourceIp 10.8.10.10 \
    --IsDefault False
```

Output: 
```
{
    "Response": {
        "RequestId": "s1609748005444321663",
        "SealId": "627caedfb394e410befc101bf0c161f2"
    }
}
```

