**Example 1: 创建 RabbitMQ 托管版实例**

创建 RabbitMQ 托管版实例

Input: 

```
tccli tdmq CreateRabbitMQVipInstance --cli-unfold-argument  \
    --ZoneIds 190001 \
    --NodeSpec rabbit-vip-basic-2 \
    --NodeNum 1 \
    --StorageSize 100 \
    --VpcId vpc-5ghsr4p9 \
    --SubnetId subnet-67y9wil4 \
    --ClusterName ApiCreate \
    --EnableCreateDefaultHaMirrorQueue False
```

Output: 
```
{
    "Response": {
        "RequestId": "a8f28d5e-a7e2-4b0b-afa0-2fba09c077a0",
        "TranId": "20230110002025620411234",
        "InstanceId": "amqp-jero744g"
    }
}
```

