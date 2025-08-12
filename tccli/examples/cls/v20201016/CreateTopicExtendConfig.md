**Example 1: 创建采集配置(clb专用)**



Input: 

```
tccli cls CreateTopicExtendConfig --cli-unfold-argument  \
    --ClbTopicExtendConfigs.0.UserAppId 1 \
    --ClbTopicExtendConfigs.0.TopicId xx \
    --ClbTopicExtendConfigs.0.UserHealthTopicId xx \
    --ClbTopicExtendConfigs.0.VpcId 1 \
    --ClbTopicExtendConfigs.0.TmpKeyExpired 1 \
    --ClbTopicExtendConfigs.0.LogSample xx \
    --ClbTopicExtendConfigs.0.UserSample xx \
    --ClbTopicExtendConfigs.0.UserTmpSecretId xx \
    --ClbTopicExtendConfigs.0.Collection True \
    --ClbTopicExtendConfigs.0.UserTmpSecretKey xx \
    --ClbTopicExtendConfigs.0.Vip xx \
    --ClbTopicExtendConfigs.0.LbKey xx \
    --ClbTopicExtendConfigs.0.UserSampleStatus True \
    --ClbTopicExtendConfigs.0.UserUin 1 \
    --ClbTopicExtendConfigs.0.UserToken xx \
    --ClbTopicExtendConfigs.0.UserTopicId xx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

