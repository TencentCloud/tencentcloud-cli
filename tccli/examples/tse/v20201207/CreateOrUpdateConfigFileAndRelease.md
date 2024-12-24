**Example 1: 创建或更新配置并发布**

创建或更新配置并发布

Input: 

```
tccli tse CreateOrUpdateConfigFileAndRelease --cli-unfold-argument  \
    --InstanceId ins-id \
    --ConfigFilePublishInfo.ReleaseName name \
    --ConfigFilePublishInfo.Namespace namespace \
    --ConfigFilePublishInfo.Group group \
    --ConfigFilePublishInfo.FileName a.yaml \
    --ConfigFilePublishInfo.Content content \
    --ConfigFilePublishInfo.Comment comment \
    --ConfigFilePublishInfo.Format yaml \
    --ConfigFilePublishInfo.CreateBy user \
    --ConfigFilePublishInfo.ModifyBy user \
    --ConfigFilePublishInfo.Tags.0.Key key \
    --ConfigFilePublishInfo.Tags.0.Value value
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

