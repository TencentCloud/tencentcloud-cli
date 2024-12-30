**Example 1: 修改投递Ckafka任务**

修改Ckafka配置

Input: 

```
tccli cls ModifyConsumer --cli-unfold-argument  \
    --TopicId fadcc986-xxxx-xxxx-b766-9ce9c193da32 \
    --Ckafka.InstanceId ckafka-xxxx \
    --Ckafka.TopicName xxxx_acl_test \
    --Ckafka.Vip 10.0.0.1 \
    --Ckafka.Vport 8080 \
    --Ckafka.InstanceName xxx_ckafka_test \
    --Ckafka.TopicId topic-maoxxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "1e5f008f-xxxx-xxxx-9636-ce13c618dfba"
    }
}
```

**Example 2: 关闭投递Ckafka任务**



Input: 

```
tccli cls ModifyConsumer --cli-unfold-argument  \
    --TopicId fadcc986-xxxx-xxxx-b766-9ce9c193da32 \
    --Effective False
```

Output: 
```
{
    "Response": {
        "RequestId": "25d826d2-xxxx-xxxx-a4b6-f5490e86ae81"
    }
}
```

