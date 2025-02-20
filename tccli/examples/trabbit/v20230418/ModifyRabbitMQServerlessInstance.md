**Example 1: 修改集群信息**

修改集群信息

Input: 

```
tccli trabbit ModifyRabbitMQServerlessInstance --cli-unfold-argument  \
    --InstanceId amqp-slmejnrgtz \
    --ClusterName dev-env \
    --Remark 测试修改
```

Output: 
```
{
    "Response": {
        "InstanceId": "amqp-slmejnrgtz",
        "RequestId": "ec77f16a-1349-4014-9eda-1cdc0b35f341"
    }
}
```

