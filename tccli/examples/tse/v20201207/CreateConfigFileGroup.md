**Example 1: 新增配置文件组**

新增配置文件组

Input: 

```
tccli tse CreateConfigFileGroup --cli-unfold-argument  \
    --InstanceId abc \
    --ConfigFileGroup.Id 1 \
    --ConfigFileGroup.Name abc \
    --ConfigFileGroup.Namespace abc \
    --ConfigFileGroup.Comment abc \
    --ConfigFileGroup.CreateTime abc \
    --ConfigFileGroup.CreateBy abc \
    --ConfigFileGroup.ModifyTime abc \
    --ConfigFileGroup.ModifyBy abc \
    --ConfigFileGroup.FileCount 1 \
    --ConfigFileGroup.UserIds abc \
    --ConfigFileGroup.GroupIds abc \
    --ConfigFileGroup.RemoveUserIds abc \
    --ConfigFileGroup.RemoveGroupIds abc \
    --ConfigFileGroup.Editable True \
    --ConfigFileGroup.Owner abc
```

Output: 
```
{
    "Response": {
        "RequestId": "jayhjxu-test-1024",
        "Result": true
    }
}
```

