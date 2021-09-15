**Example 1: 注册实名子机构并生成印章**



Input: 

```
tccli essbasic CreateSubOrganizationAndSeal --cli-unfold-argument  \
    --Caller.OperatorId erdsdf9c2a7bdcb32611f4d0200fee3d \
    --Caller.ApplicationId c17bdf9c2a7bdcb32611f4d0200fee3d \
    --Caller.SubOrganizationId 23dbdf9c2a7bdcb32611f4d0200fee3d \
    --Name TestName \
    --LegalName testName \
    --LegalIdCardType ID_CARD \
    --LegalMobile 1324567**** \
    --LegalIdCardNumber 11010119980101**** \
    --OrganizationType ENTERPRISE \
    --IdCardType USCC \
    --IdCardNumber C1505358C72DND**** \
    --SealType CONTRACT \
    --SealHorizontalText 电子签名专用章 \
    --VerifyClientIp 1.1.1.1 \
    --SealName 机构名称
```

Output: 
```
{
    "Response": {
        "SubOrganizationId": "204aa34f396f503080fe53db7406d75e",
        "RequestId": "s1609902133882212851",
        "SealId": "sd4aa34f396f503080fe53db7406d75e"
    }
}
```

