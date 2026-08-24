**Example 1: ModifyCkafkaSave**



Input: 

```
tccli csip ModifyDspmCkafkaSave --cli-unfold-argument  \
    --VipType 1 \
    --RegionId ap-guangzhou \
    --InstanceId uins-21ws \
    --InstanceName 测试资产 \
    --RouteInfo.Vip 127.0.0.1 \
    --RouteInfo.Vport 3083 \
    --RouteInfo.Domain www.root.com \
    --RouteInfo.DomainPort 3306 \
    --Username root \
    --Password root@pwd \
    --LogDeliveryInfo.0.LogType 0 \
    --LogDeliveryInfo.0.TopicId topic-2ws \
    --LogDeliveryInfo.0.TopicName send_mail
```

Output: 
```
{
    "Response": {
        "RequestId": "d0f51893-e15f-44ac-be6d-900450a6b8c2"
    }
}
```

