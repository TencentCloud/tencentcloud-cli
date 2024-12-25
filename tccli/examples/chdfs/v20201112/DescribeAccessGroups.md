**Example 1: 查看权限组列表**

查看权限组列表

Input: 

```
tccli chdfs DescribeAccessGroups --cli-unfold-argument  \
    --VpcId vpc-967aipkx
```

Output: 
```
{
    "Response": {
        "AccessGroups": [
            {
                "AccessGroupId": "ag-f8xoises",
                "AccessGroupName": "ag-test",
                "Description": "access group test",
                "VpcId": "vpc-967aipkx",
                "VpcType": 1,
                "CreateTime": "2019-07-30T16:04:30+08:00"
            }
        ],
        "RequestId": "726c9744-6e89-457e-b8c0-7008e0a1cc51"
    }
}
```

