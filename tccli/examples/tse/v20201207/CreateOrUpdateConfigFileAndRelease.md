**Example 1: 创建或更新配置并发布**

创建或更新配置并发布

Input: 

```
tccli tse CreateOrUpdateConfigFileAndRelease --cli-unfold-argument  \
    --InstanceId abc \
    --ConfigFilePublishInfo.ReleaseName abc \
    --ConfigFilePublishInfo.Namespace abc \
    --ConfigFilePublishInfo.Group abc \
    --ConfigFilePublishInfo.FileName abc \
    --ConfigFilePublishInfo.Content abc \
    --ConfigFilePublishInfo.Comment abc \
    --ConfigFilePublishInfo.Format abc \
    --ConfigFilePublishInfo.CreateBy abc \
    --ConfigFilePublishInfo.ModifyBy abc \
    --ConfigFilePublishInfo.Tags.0.Key abc \
    --ConfigFilePublishInfo.Tags.0.Value abc
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

