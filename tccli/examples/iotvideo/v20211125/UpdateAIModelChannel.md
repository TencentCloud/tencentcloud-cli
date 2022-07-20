**Example 1: 更新AI推理结果推送配置**



Input: 

```
tccli iotvideo UpdateAIModelChannel --cli-unfold-argument  \
    --CKafkaTopic test_ai_result \
    --CKafkaRegion gz \
    --CKafkaInstance ckafka-8bfqjfa \
    --ModelId body_detect \
    --Type ckafka \
    --ProductId JEOPP372CL
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "ForwardKey": ""
    }
}
```

