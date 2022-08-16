**Example 1: 查询用户组列表**

查询用户组列表

Input: 

```
tccli dasb DescribeUserGroups --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "GroupSet": [
            {
                "Department": {
                    "Managers": [
                        "121037332"
                    ],
                    "Id": "1.2.3",
                    "Name": "研发部"
                },
                "Id": 1,
                "Name": "运维组"
            }
        ],
        "RequestId": "cf80aeee-b651-4f14-9ba9-073f9f55733f"
    }
}
```

