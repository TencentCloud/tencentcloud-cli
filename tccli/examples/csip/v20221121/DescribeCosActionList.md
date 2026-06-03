**Example 1: 查看COS接口列表**



Input: 

```
tccli csip DescribeCosActionList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "req-123456789",
        "Data": [
            {
                "ActionName": "GetObject",
                "ActionNameCn": "获取对象",
                "ActionDescription": "从存储桶中获取指定对象的内容"
            },
            {
                "ActionName": "PutObject",
                "ActionNameCn": "上传对象",
                "ActionDescription": "将对象上传到指定的存储桶中"
            },
            {
                "ActionName": "DeleteObject",
                "ActionNameCn": "删除对象",
                "ActionDescription": "从存储桶中删除指定的对象"
            },
            {
                "ActionName": "ListObjects",
                "ActionNameCn": "列出对象",
                "ActionDescription": "列出存储桶中的对象列表"
            },
            {
                "ActionName": "GetBucketAcl",
                "ActionNameCn": "获取存储桶访问控制列表",
                "ActionDescription": "获取存储桶的访问控制列表配置"
            },
            {
                "ActionName": "PutBucketAcl",
                "ActionNameCn": "设置存储桶访问控制列表",
                "ActionDescription": "设置存储桶的访问控制列表"
            },
            {
                "ActionName": "GetBucketPolicy",
                "ActionNameCn": "获取存储桶策略",
                "ActionDescription": "获取存储桶的策略配置"
            },
            {
                "ActionName": "PutBucketPolicy",
                "ActionNameCn": "设置存储桶策略",
                "ActionDescription": "设置存储桶的策略配置"
            },
            {
                "ActionName": "GetBucketVersioning",
                "ActionNameCn": "获取存储桶版本控制",
                "ActionDescription": "获取存储桶的版本控制配置"
            },
            {
                "ActionName": "PutBucketVersioning",
                "ActionNameCn": "设置存储桶版本控制",
                "ActionDescription": "设置存储桶的版本控制"
            },
            {
                "ActionName": "GetBucketLifecycle",
                "ActionNameCn": "获取存储桶生命周期",
                "ActionDescription": "获取存储桶的生命周期配置"
            },
            {
                "ActionName": "PutBucketLifecycle",
                "ActionNameCn": "设置存储桶生命周期",
                "ActionDescription": "设置存储桶的生命周期规则"
            },
            {
                "ActionName": "GetBucketEncryption",
                "ActionNameCn": "获取存储桶加密",
                "ActionDescription": "获取存储桶的加密配置"
            },
            {
                "ActionName": "PutBucketEncryption",
                "ActionNameCn": "设置存储桶加密",
                "ActionDescription": "设置存储桶的加密配置"
            },
            {
                "ActionName": "GetBucketReplication",
                "ActionNameCn": "获取存储桶复制",
                "ActionDescription": "获取存储桶的复制配置"
            },
            {
                "ActionName": "PutBucketReplication",
                "ActionNameCn": "设置存储桶复制",
                "ActionDescription": "设置存储桶的复制规则"
            },
            {
                "ActionName": "GetBucketNotification",
                "ActionNameCn": "获取存储桶通知",
                "ActionDescription": "获取存储桶的通知配置"
            },
            {
                "ActionName": "PutBucketNotification",
                "ActionNameCn": "设置存储桶通知",
                "ActionDescription": "设置存储桶的通知配置"
            },
            {
                "ActionName": "GetBucketTagging",
                "ActionNameCn": "获取存储桶标签",
                "ActionDescription": "获取存储桶的标签配置"
            },
            {
                "ActionName": "PutBucketTagging",
                "ActionNameCn": "设置存储桶标签",
                "ActionDescription": "设置存储桶的标签"
            }
        ]
    }
}
```

