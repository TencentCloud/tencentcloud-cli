**Example 1: 回滚配置**

回滚配置

Input: 

```
tccli tse RollbackConfigFileReleases --cli-unfold-argument  \
    --InstanceId abc \
    --RollbackConfigFileReleases.0.Id 1 \
    --RollbackConfigFileReleases.0.Name abc \
    --RollbackConfigFileReleases.0.Namespace abc \
    --RollbackConfigFileReleases.0.Group abc \
    --RollbackConfigFileReleases.0.FileName abc \
    --RollbackConfigFileReleases.0.Content abc \
    --RollbackConfigFileReleases.0.Comment abc \
    --RollbackConfigFileReleases.0.Md5 abc \
    --RollbackConfigFileReleases.0.Version 1 \
    --RollbackConfigFileReleases.0.CreateTime abc \
    --RollbackConfigFileReleases.0.CreateBy abc \
    --RollbackConfigFileReleases.0.ModifyTime abc \
    --RollbackConfigFileReleases.0.ModifyBy abc \
    --RollbackConfigFileReleases.0.ReleaseDescription abc \
    --RollbackConfigFileReleases.0.Active True \
    --RollbackConfigFileReleases.0.Format abc
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "abc"
    }
}
```

