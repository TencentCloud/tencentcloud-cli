**Example 1: 删除配置发布**

删除配置发布

Input: 

```
tccli tse DeleteConfigFileReleases --cli-unfold-argument  \
    --InstanceId abc \
    --ConfigFileReleases.0.Namespace abc \
    --ConfigFileReleases.0.Group abc \
    --ConfigFileReleases.0.FileName abc \
    --ConfigFileReleases.0.ReleaseVersion abc
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

