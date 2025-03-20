**Example 1: 更新安全日志投递kafka设置**



Input: 

```
tccli tcss ModifySecLogDeliveryKafkaSetting --cli-unfold-argument  \
    --InstanceID ins_dhsghd \
    --InstanceName xingneng \
    --Domain www.a.com \
    --User root \
    --Password pwd \
    --RegionID ap-beijing \
    --LogTypeList.0.LogType container_bash \
    --LogTypeList.0.TopicID topicID \
    --LogTypeList.0.TopicName name \
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

