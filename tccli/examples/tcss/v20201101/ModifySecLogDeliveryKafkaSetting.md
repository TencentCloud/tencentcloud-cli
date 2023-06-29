**Example 1: 更新安全日志投递kafka设置**



Input: 

```
tccli tcss ModifySecLogDeliveryKafkaSetting --cli-unfold-argument  \
    --InstanceID 实例ID \
    --InstanceName 实例名称 \
    --Domain 域名 \
    --User 用户名 \
    --Password 密码 \
    --RegionID xxx \
    --LogTypeList.0.LogType container_bash \
    --LogTypeList.0.TopicID 主题ID \
    --LogTypeList.0.TopicName 主题名称 \
    --LogTypeList.0.State True
```

Output: 
```
{
    "Response": {
        "RequestId": "29b37d86-f63d-43d1-b21a-640e82965198"
    }
}
```

