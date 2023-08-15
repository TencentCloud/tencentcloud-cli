**Example 1: 查看安全组**

查看安全组

Input: 

```
tccli vpc DescribeSecurityGroups --cli-unfold-argument  \
    --Limit 1 \
    --Filters.0.Values TestGroup \
    --Filters.0.Name security-group-name \
    --Filters.1.Values 0 \
    --Filters.1.Name project-id
```

Output: 
```
{
    "Response": {
        "SecurityGroupSet": [
            {
                "SecurityGroupId": "sg-05bb4upy",
                "SecurityGroupName": "TestGroup",
                "SecurityGroupDesc": "test-group-desc",
                "ProjectId": "0",
                "IsDefault": true,
                "CreatedTime": "2017-04-18 21:02:30",
                "UpdateTime": "",
                "TagSet": []
            }
        ],
        "TotalCount": 1,
        "RequestId": "74883e1b-5901-46de-ae1e-d6e2cf591c5b"
    }
}
```

**Example 2: 查看绑定标签的安全组**

用tag:tag-key查询。

Input: 

```
tccli vpc DescribeSecurityGroups --cli-unfold-argument  \
    --Filters.0.Values TEST \
    --Filters.0.Name tag:Version
```

Output: 
```
{
    "Response": {
        "SecurityGroupSet": [
            {
                "SecurityGroupId": "sg-2got2lcz",
                "SecurityGroupName": "test",
                "SecurityGroupDesc": "暴露全部端口到公网和内网，有一定安全风险",
                "ProjectId": "0",
                "IsDefault": false,
                "CreatedTime": "2019-07-23 12:32:24",
                "UpdateTime": "",
                "TagSet": [
                    {
                        "Key": "中文标签键",
                        "Value": "中文标签值"
                    },
                    {
                        "Key": "Version",
                        "Value": "TEST"
                    },
                    {
                        "Key": "Version",
                        "Value": "DEV"
                    }
                ]
            }
        ],
        "TotalCount": 1,
        "RequestId": "85cda7d1-6608-4eca-8d02-19937c12dd84"
    }
}
```

