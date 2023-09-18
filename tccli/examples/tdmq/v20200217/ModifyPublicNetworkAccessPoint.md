**Example 1: RabbitMQ专享版修改公网管控台，数据流开关**



Input: 

```
tccli tdmq ModifyPublicNetworkAccessPoint --cli-unfold-argument  \
    --ClusterId amqp-testtesttest \
    --PublicNetworkAccessPointStatus True \
    --SwitchOwner Public \
    --VpcId vpc \
    --SubnetId subnetID \
    --SelectIp 10.1.0.1
```

Output: 
```
{
    "Response": {
        "RequestId": "abcd",
        "ModifyResult": "修改成功"
    }
}
```

