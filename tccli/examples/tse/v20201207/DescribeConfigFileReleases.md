**Example 1: 获取版本发布列表**

获取版本发布列表

Input: 

```
tccli tse DescribeConfigFileReleases --cli-unfold-argument  \
    --InstanceId ins-id \
    --Namespace namespace \
    --Group group \
    --FileName a.yaml \
    --OnlyUse True \
    --ReleaseName releaseName \
    --OrderField version \
    --OrderDesc desc \
    --Limit 0 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "Releases": [
            {
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
            }
        ],
        "RequestId": "req-id"
    }
}
```

