**Example 1: 创建投递Ckafka任务**

CLS 日志投递Ckafka之后，您可以对日志进行实时计算后入库。

Input: 

```
tccli cls CreateConsumer --cli-unfold-argument  \
    --TopicId 3c38e5b1-xxxx-xxxx-8963-3af704e22e73 \
    --Ckafka.Vip 10.0.0.0 \
    --Ckafka.Vport 8080 \
    --Ckafka.InstanceId ckafka-xxxx \
    --Ckafka.InstanceName ckafka_test \
    --Ckafka.TopicId topic-xxxx \
    --Ckafka.TopicName topic_test \
    --Content.EnableTag True \
    --Content.MetaFields __SOURCE__ \
    --NeedContent True \
    --Compression 0
```

Output: 
```
{
    "Response": {
        "RequestId": "6ef60xxx-xxxx-xxxx-bxxx-270359fb5xxx"
    }
}
```

