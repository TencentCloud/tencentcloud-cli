**Example 1: 查询集团账号详情**

查询集团账号详情

Input: 

```
tccli csip DescribeOrganizationInfo --cli-unfold-argument  \
    --MemberId mem-cn1***o24ca
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "NickName": "声声乌龙",
                "NodeName": "Root",
                "CFWProtect": "Ultimate",
                "WAFProtect": "",
                "CWPProtect": "Ultimate",
                "Role": "admin",
                "MemberId": "mem-625****c09**3c901",
                "JoinType": "create",
                "GroupName": "深圳市腾讯计算机系统有限公司",
                "AdminName": "2027925252",
                "AdminUin": "100014592178",
                "CreateTime": "2023-04-11 10:47:07",
                "MemberCreateTime": "2023-04-11 10:47:08",
                "NodeCount": 3,
                "MemberCount": 19,
                "SubAccountCount": 151,
                "AbnormalSubUserCount": 14,
                "GroupPayMode": 0,
                "MemberPayMode": 0,
                "GroupPermission": [
                    ""
                ],
                "MemberPermission": [
                    "查看账单",
                    "查看余额",
                    "资金划拨",
                    "合并出账",
                    "开票"
                ],
                "Departments": [
                    "Root",
                    "开发组",
                    "测试组"
                ],
                "CloudCountDesc": [
                    {
                        "CloudType": 0,
                        "CloudCount": 14,
                        "CloudDesc": "腾讯云"
                    },
                    {
                        "CloudType": 1,
                        "CloudCount": 5,
                        "CloudDesc": "AWS"
                    },
                    {
                        "CloudType": 2,
                        "CloudCount": 2,
                        "CloudDesc": "Azure"
                    }
                ],
                "EnableAdminCount": 2,
                "AdminCount": 2
            }
        ],
        "RequestId": "9c3abcf0-0860-4bd7-ae02-5825a8ee4638",
        "TotalCount": 1
    }
}
```

