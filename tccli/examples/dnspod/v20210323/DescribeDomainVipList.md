**Example 1: 获取套餐列表**

获取套餐列表

Input: 

```
tccli dnspod DescribeDomainVipList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20 \
    --Keyword dnspod
```

Output: 
```
{
    "Response": {
        "PackageList": [
            {
                "Domain": "zhaodapian.com",
                "DomainId": 12614766,
                "Downgrade": false,
                "Grade": "DP_Ultra",
                "GradeLevel": 10,
                "GradeTitle": "尊享版",
                "IsGracePeriod": "no",
                "IsSubDomain": false,
                "RemainTimes": 10,
                "ResourceId": "5032fe04",
                "SecurityInfo": {
                    "IsDefendFree": "yes",
                    "Key": "security_almighty",
                    "ResourceId": "503301e0"
                },
                "Status": "enable",
                "VipAutoRenew": "yes",
                "VipEndAt": "2024-01-16 15:56:31",
                "VipStartAt": "2023-01-16 15:56:31"
            },
            {
                "Domain": null,
                "DomainId": 0,
                "Downgrade": false,
                "Grade": "DP_Plus",
                "GradeLevel": 3,
                "GradeTitle": "专业版",
                "IsGracePeriod": "no",
                "IsSubDomain": null,
                "RemainTimes": 10,
                "ResourceId": "9bae4aaf",
                "SecurityInfo": null,
                "Status": "enable",
                "VipAutoRenew": "default",
                "VipEndAt": "2023-12-14 20:00:36",
                "VipStartAt": "2022-12-14 20:01:48"
            },
            {
                "Domain": "yyds3.com",
                "DomainId": 12620578,
                "Downgrade": true,
                "Grade": "DP_Ultra",
                "GradeLevel": 10,
                "GradeTitle": "尊享版",
                "IsGracePeriod": "no",
                "IsSubDomain": false,
                "RemainTimes": 7,
                "ResourceId": "99a1869f",
                "SecurityInfo": {
                    "IsDefendFree": "yes",
                    "Key": "security_almighty",
                    "ResourceId": "9ba4b170"
                },
                "Status": "enable",
                "VipAutoRenew": "default",
                "VipEndAt": "2023-12-14 17:40:40",
                "VipStartAt": "2022-12-14 20:37:48"
            },
            {
                "Domain": "aaaa.cn",
                "DomainId": 12613589,
                "Downgrade": false,
                "Grade": "DP_Ultra",
                "GradeLevel": 10,
                "GradeTitle": "尊享版",
                "IsGracePeriod": "no",
                "IsSubDomain": false,
                "RemainTimes": 0,
                "ResourceId": "a0bed80e",
                "SecurityInfo": {
                    "IsDefendFree": "yes",
                    "Key": "security_almighty",
                    "ResourceId": "a0bedda5"
                },
                "Status": "enable",
                "VipAutoRenew": "default",
                "VipEndAt": "2023-04-28 11:37:17",
                "VipStartAt": "2022-12-02 15:50:50"
            },
            {
                "Domain": null,
                "DomainId": 0,
                "Downgrade": true,
                "Grade": "DP_Extra",
                "GradeLevel": 6,
                "GradeTitle": "企业基础版",
                "IsGracePeriod": "yes",
                "IsSubDomain": null,
                "RemainTimes": 1,
                "ResourceId": "5a8fb3ea",
                "SecurityInfo": null,
                "Status": "enable",
                "VipAutoRenew": "default",
                "VipEndAt": "2023-02-23 11:24:43",
                "VipStartAt": "2022-12-02 15:51:17"
            },
            {
                "Domain": "jd.com",
                "DomainId": 12600783,
                "Downgrade": true,
                "Grade": "DP_Ultra",
                "GradeLevel": 10,
                "GradeTitle": "尊享版",
                "IsGracePeriod": "yes",
                "IsSubDomain": false,
                "RemainTimes": 10,
                "ResourceId": "5a160c26",
                "SecurityInfo": {
                    "IsDefendFree": "yes",
                    "Key": "security_almighty",
                    "ResourceId": "5a79443c"
                },
                "Status": "enable",
                "VipAutoRenew": "default",
                "VipEndAt": "2023-02-23 10:52:16",
                "VipStartAt": "2022-02-23 10:52:16"
            }
        ],
        "RequestId": "bbe13f12-dfeb-4e19-8668-3eb8c828cefc",
        "TotalCount": 6
    }
}
```

