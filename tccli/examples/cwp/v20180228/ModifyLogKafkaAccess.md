**Example 1: 示例**



Input: 

```
tccli cwp ModifyLogKafkaAccess --cli-unfold-argument  \
    --Username a \
    --VpcId 1.1.1.1 \
    --Zone 广州 \
    --KafkaId aa \
    --InsVersion 1.1.1 \
    --AccessType 1 \
    --KafkaEnvName 云镜测试环境 \
    --BandWidth 300 \
    --AccessAddr 1.1.1.1 \
    --Pwd b \
    --DiskSize 400 \
    --SubnetId 1.1.1.1 \
    --DeliverTypeDetails.0.Status 0 \
    --DeliverTypeDetails.0.TopicId xx \
    --DeliverTypeDetails.0.SecurityType 1 \
    --DeliverTypeDetails.0.LogType 1 \
    --DeliverTypeDetails.0.Switch 0 \
    --DeliverTypeDetails.0.StatusTime 11 \
    --DeliverTypeDetails.0.TopicName xx \
    --DeliverTypeDetails.0.ErrInfo x \
    --Az 广州三区 \
    --DeliverStatus 1 \
    --HasPwd 1
```

Output: 
```
{
    "Response": {
        "RequestId": "fee0ea18-d002-4af0-bee3-7f6efd19e357"
    }
}
```

