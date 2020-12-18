**Example 1: 查看权限组详细信息**

查看权限组详细信息

Input: 

```
tccli chdfs DescribeAccessGroup --cli-unfold-argument  \
    --AccessGroupId ag-f8xoises
```

Output: 
```
{
    "Response": {
        "AccessGroup": {
            "AccessGroupId": "ag-f8xoises",
            "AccessGroupName": "test",
            "Description": "test",
            "VpcType": 1,
            "VpcId": "vpc-967aipkx",
            "CreateTime": "2019-07-30T16:04:30+08:00"
        },
        "RequestId": "ab3fff6b-7a36-4b7f-b2bb-bba87b5945a6"
    }
}
```

