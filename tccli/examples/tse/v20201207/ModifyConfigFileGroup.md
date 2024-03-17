**Example 1: 修改配置文件组详情**

批量修改配置文件组

Input: 

```
tccli tse ModifyConfigFileGroup --cli-unfold-argument  \
    --InstanceId abc \
    --ConfigFileGroup.Name abc \
    --ConfigFileGroup.Namespace abc \
    --ConfigFileGroup.Comment abc \
    --ConfigFileGroup.FileCount 1 \
    --ConfigFileGroup.UserIds abc \
    --ConfigFileGroup.GroupIds abc \
    --ConfigFileGroup.RemoveUserIds abc \
    --ConfigFileGroup.RemoveGroupIds abc
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

