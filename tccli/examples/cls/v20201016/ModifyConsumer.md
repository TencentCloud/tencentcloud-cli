**Example 1: 修改投递Ckafka任务**

修改Ckafka配置

Input: 

```
tccli cls ModifyConsumer --cli-unfold-argument  \
    --TopicId 871710c5-35cd-4d1e-8e79-2fa92c35d612 \
    --Ckafka.InstanceId ckafka-8j4az592 \
    --Ckafka.TopicName xxxx_acl_demo \
    --Ckafka.Vip 127.0.0.1 \
    --Ckafka.Vport 8080 \
    --Ckafka.InstanceName ckafka_test \
    --Ckafka.TopicId topic-jmpmwe12
```

Output: 
```
{
    "Response": {
        "RequestId": "cfde6389-f546-4676-8900-ad3d304cbb54"
    }
}
```

**Example 2: 关闭投递Ckafka任务**



Input: 

```
tccli cls ModifyConsumer --cli-unfold-argument  \
    --TopicId 871710c5-35cd-4d1e-8e79-2fa92c35d612 \
    --Effective False
```

Output: 
```
{
    "Response": {
        "RequestId": "24c19d3a-9444-4b0a-a1bd-53a87fa50bc5"
    }
}
```

