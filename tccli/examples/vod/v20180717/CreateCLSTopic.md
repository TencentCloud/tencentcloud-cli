**Example 1: 创建一个新的日志主题**



Input: 

```
tccli vod CreateCLSTopic --cli-unfold-argument  \
    --CLSRegion ap-guangzhou \
    --TopicName mytopic \
    --LogsetId 54079098-61ea-48f9-8270-3b041a5d0150
```

Output: 
```
{
    "Response": {
        "TopicId": "780ba384-5bc1-4cb1-a0e9-0cf8fafd3ee0",
        "RequestId": "xxx"
    }
}
```

