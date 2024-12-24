**Example 1: 创建权限组**

创建权限组

Input: 

```
tccli chdfs CreateAccessGroup --cli-unfold-argument  \
    --AccessGroupName access-group-test \
    --VpcType 1 \
    --VpcId vpc-0q1uxxxx \
    --Description create access group example
```

Output: 
```
{
    "Response": {
        "AccessGroup": {
            "AccessGroupId": "ag-gei2xxxx",
            "AccessGroupName": "access-group-test",
            "CreateTime": "2024-12-24T20:00:47+08:00",
            "Description": "create access group example",
            "VpcId": "vpc-0q1uxxxx",
            "VpcType": 1
        },
        "RequestId": "c363615f-1e62-49e8-b768-0606e75d2e5d"
    }
}
```

