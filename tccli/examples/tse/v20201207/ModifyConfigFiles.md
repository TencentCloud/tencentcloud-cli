**Example 1: 修改配置文件**

修改配置文件

Input: 

```
tccli tse ModifyConfigFiles --cli-unfold-argument  \
    --InstanceId ins-id \
    --ConfigFile.Id 1 \
    --ConfigFile.Name name \
    --ConfigFile.Namespace namespace \
    --ConfigFile.Group group \
    --ConfigFile.Content content \
    --ConfigFile.Format yaml \
    --ConfigFile.Comment comment \
    --ConfigFile.Status status \
    --ConfigFile.Tags.0.Key key \
    --ConfigFile.Tags.0.Value value \
    --ConfigFile.CreateTime 2024-10-08 10:00:00 \
    --ConfigFile.CreateBy user \
    --ConfigFile.ModifyTime 2024-10-08 10:00:00 \
    --ConfigFile.ModifyBy user \
    --ConfigFile.ReleaseTime 2024-10-08 10:00:00 \
    --ConfigFile.ReleaseBy user
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "req-id"
    }
}
```

