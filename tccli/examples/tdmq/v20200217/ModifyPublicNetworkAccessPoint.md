**Example 1: RabbitMQ专享版修改公网管控台，数据流开关**



Input: 

```
tccli tdmq ModifyPublicNetworkAccessPoint --cli-unfold-argument  \
    --ClusterId amqp-test \
    --PublicNetworkAccessPointStatus True \
    --SwitchOwner Public \
    --VpcId vpc-d \
    --SubnetId subnet-test \
    --SelectIp 10.1.0.1
```

Output: 
```
{
    "Response": {
        "RequestId": "a8f28d5e-a7e2-4b0b-afa0-2fba09c077a0",
        "ModifyResult": "修改成功"
    }
}
```

