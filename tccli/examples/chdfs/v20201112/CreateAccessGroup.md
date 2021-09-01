**Example 1: 创建权限组**

创建权限组

Input: 

```
tccli chdfs CreateAccessGroup --cli-unfold-argument  \
    --AccessGroupName test \
    --Description test \
    --VpcType 1 \
    --VpcId vpc-967aipkx
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

