**Example 1: 新增配置文件组**

新增配置文件组

Input: 

```
tccli tse CreateConfigFileGroup --cli-unfold-argument  \
    --InstanceId ins-id \
    --ConfigFileGroup.Id 1 \
    --ConfigFileGroup.Name name \
    --ConfigFileGroup.Namespace namespace \
    --ConfigFileGroup.Comment comment \
    --ConfigFileGroup.CreateTime 2024-10-08 10:00:00 \
    --ConfigFileGroup.CreateBy user \
    --ConfigFileGroup.ModifyTime 2024-10-08 10:00:00 \
    --ConfigFileGroup.ModifyBy user \
    --ConfigFileGroup.FileCount 1 \
    --ConfigFileGroup.UserIds 101 \
    --ConfigFileGroup.GroupIds groupa \
    --ConfigFileGroup.RemoveUserIds 101 \
    --ConfigFileGroup.RemoveGroupIds groupa \
    --ConfigFileGroup.Editable True \
    --ConfigFileGroup.Owner 101
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

