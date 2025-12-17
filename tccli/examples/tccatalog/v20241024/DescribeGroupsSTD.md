**Example 1: 获取组**

获取组

Input: 

```
tccli tccatalog DescribeGroupsSTD --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "GroupName": "角色名称不能为空的"
            },
            {
                "GroupName": "test_create"
            },
            {
                "GroupName": "Admin"
            }
        ],
        "RequestId": "c52b3336-3709-458e-b425-a57ed5892696",
        "TotalCount": 3
    }
}
```

