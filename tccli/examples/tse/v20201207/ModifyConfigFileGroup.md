**Example 1: 修改配置文件组详情**

批量修改配置文件组

Input: 

```
tccli tse ModifyConfigFileGroup --cli-unfold-argument  \
    --InstanceId ins-id \
    --ConfigFileGroup.Name name \
    --ConfigFileGroup.Namespace namespace \
    --ConfigFileGroup.Comment comment \
    --ConfigFileGroup.FileCount 1 \
    --ConfigFileGroup.UserIds 101 \
    --ConfigFileGroup.GroupIds groupa \
    --ConfigFileGroup.RemoveUserIds 101 \
    --ConfigFileGroup.RemoveGroupIds groupa
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "63d46143-c731-4aff-b0c9-edce7401db32"
    }
}
```

