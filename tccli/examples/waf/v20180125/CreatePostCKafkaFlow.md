**Example 1: 创建CLS投递流任务**



Input: 

```
tccli waf CreatePostCKafkaFlow --cli-unfold-argument  \
    --WriteConfig.EnableHeaders 1 \
    --WriteConfig.EnableBody 1 \
    --Compression snappy \
    --CKafkaID ckafka-2v4rkwpg \
    --KafkaVersion 1.1.1 \
    --Topic waf-topic \
    --LogType 1 \
    --CKafkaRegion ap-guangzho \
    --SASLUser ckafka-2v4rkwpg# \
    --Brokers 11.179.226.202:6142 \
    --SASLPassword  \
    --SASLEnable 0 \
    --VipType 2
```

Output: 
```
{
    "Response": {
        "RequestId": "4c3a2707-619c-4943-ae91-2f855c0125a6"
    }
}
```

