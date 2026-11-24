**Example 1: 获取组织详情**



Input: 

```
tccli organization DescribeOrganization --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "CreateTime": "2026-07-28 19:04:01",
        "DefaultPayType": "SelfPay",
        "HostUin": 700002783413,
        "IsAllowQuit": "Denied",
        "IsAssignManager": false,
        "IsAuthManager": true,
        "IsManager": true,
        "JoinTime": "2026-07-28 19:04:01",
        "MemberPermissionOptions": [
            {
                "DefaultChecked": true,
                "DisabledCode": "",
                "Id": 1,
                "Name": "查看账单",
                "Status": "FIXED"
            },
            {
                "DefaultChecked": true,
                "DisabledCode": "",
                "Id": 2,
                "Name": "查看余额",
                "Status": "FIXED"
            },
            {
                "DefaultChecked": false,
                "DisabledCode": "TransferNotAllowAdd",
                "Id": 3,
                "Name": "资金划拨",
                "Status": "DISABLE"
            },
            {
                "DefaultChecked": true,
                "DisabledCode": "",
                "Id": 4,
                "Name": "合并出账",
                "Status": "OPTIONAL"
            },
            {
                "DefaultChecked": false,
                "DisabledCode": "",
                "Id": 5,
                "Name": "开票",
                "Status": "OPTIONAL"
            },
            {
                "DefaultChecked": false,
                "DisabledCode": "",
                "Id": 7,
                "Name": "代付费",
                "Status": "OPTIONAL"
            },
            {
                "DefaultChecked": false,
                "DisabledCode": "",
                "Id": 8,
                "Name": "成本分析",
                "Status": "OPTIONAL"
            },
            {
                "DefaultChecked": false,
                "DisabledCode": "",
                "Id": 9,
                "Name": "预算管理",
                "Status": "OPTIONAL"
            },
            {
                "DefaultChecked": false,
                "DisabledCode": "CreditAmountsNotAllowAdd",
                "Id": 10,
                "Name": "信用额度设置",
                "Status": "DISABLE"
            }
        ],
        "NickName": "700002783413",
        "OrgId": 211346,
        "OrgPermission": [
            {
                "Id": 1,
                "Name": "允许组织管理员查看成员账号的财务信息"
            },
            {
                "Id": 2,
                "Name": "允许组织管理员查看成员账号的消费信息"
            },
            {
                "Id": 4,
                "Name": "允许组织管理员合并出账"
            },
            {
                "Id": 5,
                "Name": "允许组织管理员代成员账号开票"
            }
        ],
        "OrgPolicyName": "财务管理",
        "OrgPolicyType": "Financial",
        "OrgType": 1,
        "PayName": "",
        "PayUin": "",
        "RequestId": "d0326601-a3cd-4524-848c-7da13ccf0af9",
        "RootNodeId": 224674
    }
}
```

