**Example 1: 删除配置发布**

删除配置发布

Input: 

```
tccli tse DeleteConfigFileReleases --cli-unfold-argument  \
    --InstanceId ins-id \
    --ConfigFileReleases.0.Namespace namespace \
    --ConfigFileReleases.0.Group group \
    --ConfigFileReleases.0.FileName a.yaml \
    --ConfigFileReleases.0.ReleaseVersion 1.0
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

