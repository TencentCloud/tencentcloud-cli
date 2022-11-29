**Example 1: 创建自学习模型**



Input: 

```
tccli asr CreateCustomization --cli-unfold-argument  \
    --ModelName 自学习模型 \
    --ModelType 16k \
    --TextUrl http://www.download.com/test.txt
```

Output: 
```
{
    "Response": {
        "RequestId": "a23740a1-4bb5-4154-9f1f-ea36b1bfe2ea",
        "ModelId": "413c479df72d11eaacd3c81fbecfd0bd"
    }
}
```

