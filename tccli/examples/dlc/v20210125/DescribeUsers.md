**Example 1: 获取用户列表信息**



Input: 

```
tccli dlc DescribeUsers --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 222,
        "UserSet": [
            {
                "AccountType": "UserAccount",
                "CreateTime": "2025-11-08 12:04:14",
                "Creator": "700002195687",
                "IsOwner": false,
                "PolicySet": [],
                "UserAlias": "thea_004",
                "UserDescription": "",
                "UserId": "700002220057",
                "UserType": "COMMON",
                "WorkGroupSet": []
            }
        ],
        "RequestId": "fe51b336-c33f-4c34-8334-eb4afe0ee127"
    }
}
```

