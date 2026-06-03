**Example 1: 创建从MQTT到RocketMQ集群的Topic数据复制任务**

创建从MQTT到RocketMQ集群的Topic数据复制任务

Input: 

```
tccli tdmq CreateRocketMQRouterRule --cli-unfold-argument  \
    --StartNow True \
    --Rule.SourceType TENCENT_MQTT \
    --Rule.TargetType TENCENT_ROCKETMQ \
    --Rule.RemarkName test-rmq-mqtt-sync \
    --Rule.TenRocketMQTarget.Topic true \
    --Rule.TenRocketMQTarget.ClusterId rmq-16vjxq59j2 \
    --Rule.TenRocketMQTarget.TargetRegion ap-chengdu \
    --Rule.TenRocketMQTarget.RoleName test_ben \
    --Rule.TenRocketMQTarget.AccessKey testak16vcb04be9d04 \
    --Rule.TenRocketMQTarget.SecretKey testskca1f0368ee4 \
    --Rule.TenMQTTSource.ClusterId mqtt-embkr9ar \
    --Rule.TenMQTTSource.Topic mqtt-topic-6 \
    --Rule.TenMQTTSource.SourceRegion ap-chengdu \
    --Rule.TenMQTTSource.UserName dev-user \
    --Rule.TenMQTTSource.Password 123qweASD123 \
    --Rule.TenMQTTSource.Endpoint mqtt-embkr9ar-gz-internal.mqtt.tencenttdmq.com:1883 \
    --SyncType Topic
```

Output: 
```
{
    "Response": {
        "RequestId": "46d960fa-5761-41ae-b908-4d023c7d3511"
    }
}
```

