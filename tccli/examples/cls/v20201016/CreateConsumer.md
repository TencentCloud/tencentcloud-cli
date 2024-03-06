**Example 1: 创建投递Ckafka任务**

CLS 日志投递Ckafka之后，您可以对日志进行实时计算后入库。

Input: 

```
tccli cls CreateConsumer --cli-unfold-argument  \
    --TopicId xxx-xxx-xxx-xxx \
    --Ckafka.Vip 10.123.123.123 \
    --Ckafka.Vport 8888 \
    --Ckafka.InstanceId xxxxx \
    --Ckafka.InstanceName myname \
    --Ckafka.TopicId xxxxx \
    --Ckafka.TopicName xxxxx \
    --Content.EnableTag True \
    --Content.MetaFields __SOURCE__ \
    --NeedContent True \
    --Compression 0
```

Output: 
```
{
    "Response": {
        "RequestId": "6ef60xxx-0xxx-4xxx-bxxx-270359fb5xxx"
    }
}
```

