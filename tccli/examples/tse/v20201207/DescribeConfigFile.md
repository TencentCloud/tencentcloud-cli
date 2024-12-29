**Example 1: 查询单个配置文件详细**

查询单个配置文件详细

Input: 

```
tccli tse DescribeConfigFile --cli-unfold-argument  \
    --InstanceId ins-id \
    --Namespace namespace \
    --Group group \
    --Name name
```

Output: 
```
{
    "Response": {
        "ConfigFile": {
            "Id": 1,
            "Name": "name",
            "Namespace": "namespace",
            "Group": "group",
            "Content": "content",
            "Format": "yaml",
            "Comment": "comment",
            "Status": "status",
            "Tags": [
                {
                    "Key": "key",
                    "Value": "value"
                }
            ],
            "CreateTime": "2024-10-08 10:00:00",
            "CreateBy": "user",
            "ModifyTime": "2024-10-08 10:00:00",
            "ModifyBy": "user",
            "ReleaseTime": "2024-10-08 10:00:00",
            "ReleaseBy": "user"
        },
        "RequestId": "req-id"
    }
}
```

