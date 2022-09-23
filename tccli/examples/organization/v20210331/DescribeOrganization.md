**Example 1: 获取组织详情**



Input: 

```
tccli organization DescribeOrganization --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "CreateTime": "2021-04-15 21:07:54",
        "JoinTime": "2021-04-15 21:07:54",
        "HostUin": 100000546922,
        "IsManager": true,
        "NickName": "",
        "OrgId": 13,
        "OrgPermission": [
            {
                "Id": 1,
                "Name": "允许主账号查看子账号的消费信息"
            },
            {
                "Id": 2,
                "Name": "允许主账号查看子账号的财务信息"
            },
            {
                "Id": 3,
                "Name": "允许主账号划拨资金给子账号"
            },
            {
                "Id": 4,
                "Name": "允许主账号对子账号的账单合并出账"
            },
            {
                "Id": 5,
                "Name": "允许主账号代子账号开票"
            }
        ],
        "OrgPolicyName": "财务管理",
        "OrgPolicyType": "Financial",
        "OrgType": 1,
        "RootNodeId": 1001,
        "IsAllowQuit": "Allow",
        "PayUin": "",
        "PayName": "",
        "IsAssignManager": false,
        "IsAuthManager": false,
        "RequestId": "e5c09721-236b-4a55-a5d1-0513ac506245"
    }
}
```

