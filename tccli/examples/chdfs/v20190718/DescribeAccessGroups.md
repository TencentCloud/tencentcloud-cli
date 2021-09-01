**Example 1: 查看权限组列表**

查看权限组列表

Input: 

```
tccli chdfs DescribeAccessGroups --cli-unfold-argument  \
    --Offset 0 \
    --Limit 1 \
    --Filters.0.Name AccessGroupName \
    --Filters.0.Values test \
    --Filters.1.Name AccessGroupId \
    --Filters.1.Values ag-f8xoises
```

Output: 
```
{
    "Response": {
        "AccessGroups": [
            {
                "AccessGroupId": "ag-f8xoises",
                "AccessGroupName": "test",
                "Description": "test",
                "CreateTime": "2019-07-30T16:04:30+08:00"
            }
        ],
        "RequestId": "726c9744-6e89-457e-b8c0-7008e0a1cc51"
    }
}
```

