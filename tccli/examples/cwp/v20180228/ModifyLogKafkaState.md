**Example 1: 修改日志投递状态信息**



Input: 

```
tccli cwp ModifyLogKafkaState --cli-unfold-argument  \
    --KafkaEnvName 主机安全测试环境 \
    --KafkaId ckafka-ce80kte5 \
    --AccessType 1 \
    --AccessAddr 127.0.0.1:80 \
    --Username 12 \
    --Zone 广州 \
    --Az 广州三区 \
    --VpcId vpc-ad* \
    --SubnetId subnet-* \
    --DeliverStatus 1 \
    --InsVersion 0.10.2.1 \
    --BandWidth 1200 \
    --DiskSize 2500
```

Output: 
```
{
    "Response": {
        "RequestId": "29b37d86-f63d-43d1-b21a-640e82965198"
    }
}
```

