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
        "HostUin": 1001,
        "IsManager": true,
        "NickName": "host_name",
        "OrgId": 101,
        "OrgPermission": [
            {
                "Id": 1,
                "Name": "viewBill"
            },
            {
                "Id": 2,
                "Name": "viewBalance"
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

