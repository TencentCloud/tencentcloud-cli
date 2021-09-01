**Example 1: 查看AI推理结果推送配置**



Input: 

```
tccli iotvideo DescribeAIModelChannel --cli-unfold-argument  \
    --ProductId test \
    --ModelId body_detect
```

Output: 
```
{
    "Response": {
        "ForwardKey": "",
        "ForwardAddress": "",
        "CKafkaTopic": "test_ai_result",
        "CKafkaRegion": "gz",
        "RequestId": "xx",
        "CKafkaInstance": "ckafka-insfeae",
        "Type": "ckafka"
    }
}
```

