**Example 1: 创建子企业或机构信息**



Input: 

```
tccli essbasic CreateSubOrganization --cli-unfold-argument  \
    --Caller.OperatorId  \
    --Caller.ApplicationId c17bdf9c2a7bdcb32611f4d0200fee3d \
    --Caller.SubOrganizationId  \
    --Name 机构名称 \
    --LegalName 法人或联系人姓名 \
    --LegalIdCardType ID_CARD \
    --LegalMobile 1324567**** \
    --LegalIdCardNumber 11010119980101**** \
    --OrganizationType ENTERPRISE \
    --IdCardType USCC \
    --IdCardNumber C1505358C72DN***** \
    --UseOpenId True \
    --OpenId 204aa34f396f503080fe53db7406d75e
```

Output: 
```
{
    "Response": {
        "SubOrganizationId": "204aa34f396f503080fe53db7406d75e",
        "RequestId": "s1609902133882212851"
    }
}
```

