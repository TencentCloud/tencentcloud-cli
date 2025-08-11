**Example 1: 创建投递Ckafka任务**

CLS 日志投递Ckafka之后，您可以对日志进行实时计算后入库。

Input: 

```
tccli cls CreateConsumer --cli-unfold-argument  \
    --TopicId 871710c5-35cd-4d1e-8e79-2fa92c35d612 \
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
        "RequestId": "5beb8d61-93b9-417b-85a3-4d7db8f7618a"
    }
}
```

