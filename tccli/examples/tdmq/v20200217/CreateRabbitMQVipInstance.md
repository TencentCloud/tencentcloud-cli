**Example 1: 创建RabbitMQ专享版实例**

创建RabbitMQ专享版实例

Input: 

```
tccli tdmq CreateRabbitMQVipInstance --cli-unfold-argument  \
    --ZoneIds 190001 \
    --NodeSpec rabbit-vip-basic-2 \
    --NodeNum 1 \
    --StorageSize 100 \
    --VpcId vpc-xxx \
    --SubnetId subnet-xxx \
    --ClusterName ApiCreate \
    --EnableCreateDefaultHaMirrorQueue False
```

Output: 
```
{
    "Response": {
        "RequestId": "sadasfdsfs",
        "TranId": "20230110002025620411234",
        "InstanceId": "amqp-aegnagjg"
    }
}
```

