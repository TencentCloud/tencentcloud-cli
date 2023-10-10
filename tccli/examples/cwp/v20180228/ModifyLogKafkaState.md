**Example 1: 修改日志投递状态信息**



Input: 

```
tccli cwp ModifyLogKafkaState --cli-unfold-argument  \
    --KafkaEnvName 云镜测试环境 \
    --KafkaId ckafka-ce80kte5 \
    --AccessType 1 \
    --AccessAddr 127.0.0.1:80 \
    --Username xx \
    --Zone 广州 \
    --Az 广州三区 \
    --VpcId - \
    --SubnetId - \
    --DeliverStatus 1 \
    --InsVersion 0.10.2.1 \
    --BandWidth 1200 \
    --DiskSize 2500
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

