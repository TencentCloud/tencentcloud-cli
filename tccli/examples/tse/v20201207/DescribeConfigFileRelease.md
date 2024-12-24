**Example 1: 查询配置文件发布详情**

查询配置文件发布详情

Input: 

```
tccli tse DescribeConfigFileRelease --cli-unfold-argument  \
    --InstanceId ins-fd191a86 \
    --Namespace Polaris \
    --Group group-test-jayhjxu \
    --Name config-file-test
```

Output: 
```
{
    "Response": {
        "ConfigFileRelease": {
            "Id": 1,
            "Name": "name",
            "Namespace": "namespace",
            "Group": "group",
            "FileName": "a.yaml",
            "Content": "content",
            "Comment": "comment",
            "Md5": "hash",
            "Version": 1,
            "CreateTime": "2024-10-08 10:00:00",
            "CreateBy": "user",
            "ModifyTime": "2024-10-08 10:00:00",
            "ModifyBy": "user",
            "ReleaseDescription": "desc",
            "Active": true,
            "Format": "yaml"
        },
        "RequestId": "req-id"
    }
}
```

