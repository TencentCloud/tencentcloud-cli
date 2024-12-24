**Example 1: 回滚配置**

回滚配置

Input: 

```
tccli tse RollbackConfigFileReleases --cli-unfold-argument  \
    --InstanceId ins-id \
    --RollbackConfigFileReleases.0.Id 1 \
    --RollbackConfigFileReleases.0.Name name \
    --RollbackConfigFileReleases.0.Namespace namespace \
    --RollbackConfigFileReleases.0.Group group \
    --RollbackConfigFileReleases.0.FileName a.yaml \
    --RollbackConfigFileReleases.0.Content content \
    --RollbackConfigFileReleases.0.Comment comment \
    --RollbackConfigFileReleases.0.Md5 hash \
    --RollbackConfigFileReleases.0.Version 1 \
    --RollbackConfigFileReleases.0.CreateTime 2024-10-08 10:00:00 \
    --RollbackConfigFileReleases.0.CreateBy user \
    --RollbackConfigFileReleases.0.ModifyTime 2024-10-08 10:00:00 \
    --RollbackConfigFileReleases.0.ModifyBy user \
    --RollbackConfigFileReleases.0.ReleaseDescription desc \
    --RollbackConfigFileReleases.0.Active True \
    --RollbackConfigFileReleases.0.Format yaml
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

