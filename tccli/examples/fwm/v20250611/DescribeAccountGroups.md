**Example 1: 获取账户组列表**



Input: 

```
tccli fwm DescribeAccountGroups --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "AccountGroups": [
            {
                "CreateTime": "2026-03-18 22:39:17",
                "Description": "生产账号组",
                "GroupId": "acg-rwqqudnm",
                "GroupName": "生产账号组1组",
                "MemberCount": 1
            }
        ],
        "RequestId": "01e1ef16-2d81-4555-879a-24774b388dda",
        "TotalCount": 1
    }
}
```

