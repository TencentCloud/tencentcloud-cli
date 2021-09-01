**Example 1: 配置产品转发消息队列**



Input: 

```
tccli iotvideo SetMessageQueue --cli-unfold-argument  \
    --ProductId 12345678910 \
    --MsgQueueType 2 \
    --MsgType 0,1,2,3,4,5 \
    --Topic testTopic \
    --Instance testInstance \
    --MsgRegion xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "1e2aa138-e61c-4fba-a60a-a6505624799a"
    }
}
```

