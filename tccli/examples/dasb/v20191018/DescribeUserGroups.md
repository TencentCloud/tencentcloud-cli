**Example 1: 查询用户组列表**

查询用户组列表

Input: 

```
tccli dasb DescribeUserGroups --cli-unfold-argument  \
    --IdSet 1 \
    --Name 测试组 \
    --Offset 1 \
    --Limit 1 \
    --DepartmentId 1.3
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "GroupSet": [
            {
                "Id": 1,
                "Name": "研发组",
                "Department": {
                    "Id": "1.2",
                    "Name": "运营组",
                    "Managers": [
                        "12345642122132"
                    ],
                    "ManagerUsers": [
                        {
                            "ManagerId": "2457130554035",
                            "ManagerName": "carl"
                        }
                    ]
                },
                "Count": 1
            }
        ],
        "RequestId": "cf80aeee-b651-4f14-9ba9-073f9f55733f"
    }
}
```

