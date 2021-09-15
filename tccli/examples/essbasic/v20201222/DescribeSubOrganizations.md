**Example 1: 查询子机构信息**



Input: 

```
tccli essbasic DescribeSubOrganizations --cli-unfold-argument  \
    --SubOrganizationIds 3768438f76ea49b43b8c819b13438ae3 \
    --Caller.OperatorId dolore \
    --Caller.ApplicationId c17bdf9c2a7bdcb32611f4d0200fee3d \
    --Caller.SubOrganizationId 
```

Output: 
```
{
    "Response": {
        "RequestId": "s1610021101589519007",
        "SubOrganizationInfos": [
            {
                "BizLicenseFile": "",
                "BizLicenseFileName": "quis sed",
                "ContactAddress": {
                    "City": "",
                    "Country": "",
                    "County": "",
                    "Details": "",
                    "Province": ""
                },
                "ContactName": "",
                "CreatedOn": 1610021071,
                "Email": "",
                "Id": "3768438f76ea49b43b8c819b13438ae3",
                "IdCardFileType": "",
                "IdCardNumber": "567898765678",
                "IdCardType": "USCC",
                "LegalIdCardNumber": "7LDRplp3PmNCJ75vMjbzsuCy2qOi7RAf2YCIZk6v8Ck=",
                "LegalIdCardType": "ID_CARD",
                "LegalMobile": "13245678986",
                "LegalName": "测试机构那",
                "Name": "in minim",
                "OrganizationType": "ENTERPRISE",
                "UpdatedOn": 0,
                "VerifiedOn": 0,
                "VerifyClientIp": "",
                "VerifyServerIp": "",
                "VerifyStatus": "NotVerified"
            }
        ]
    }
}
```

