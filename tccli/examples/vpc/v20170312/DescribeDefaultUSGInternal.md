**Example 1: 获取默认安全组**



Input: 

```
tccli vpc DescribeDefaultUSGInternal --cli-unfold-argument  \
    --SgId 1234567 \
    --ProjectId 12121 \
    --UsgRemark remark \
    --UsgName test
```

Output: 
```
{
    "Response": {
        "ProjectId": "133",
        "SgName": "default",
        "New": 0,
        "Sys": 1,
        "AppId": "123009212",
        "SafeGroupId": "sg-llk3kg2x",
        "Os": 0,
        "CreateTime": "2022-06-22 10:43:42",
        "SgRemark": "System created security group",
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

**Example 2: demo**



Input: 

```
tccli vpc DescribeDefaultUSGInternal --cli-unfold-argument  \
    --UsgName default \
    --ProjectId 133 \
    --UsgRemark System created security group \
    --SgId 123009212
```

Output: 
```
{
    "Response": {
        "ProjectId": "133",
        "SgName": "default",
        "New": 0,
        "Sys": 1,
        "AppId": "123009212",
        "SafeGroupId": "sg-llk3kg2x",
        "Os": 0,
        "CreateTime": "2022-06-22 10:43:42",
        "SgRemark": "System created security group",
        "RequestId": "c2773d95-a87d-4098-8c17-3b13f0bbd512"
    }
}
```

