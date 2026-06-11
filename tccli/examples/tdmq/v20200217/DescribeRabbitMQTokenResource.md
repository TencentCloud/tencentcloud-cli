**Example 1: 查询开启cam验证的RabbitMQ资源**



Input: 

```
tccli tdmq DescribeRabbitMQTokenResource --cli-unfold-argument  \
    --UserResourceId amqp-ogmrjdk5 \
    --ResourceAccount test_cjq \
    --InstanceType rabbitmq \
    --ResourceRegion ap-guangzhou \
    --AccountHost %
```

Output: 
```
{
    "Response": {
        "EnabledRotate": true,
        "RequestId": "d71ad677-f943-47dc-aeca-1da0379a81d4"
    }
}
```

