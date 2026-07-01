**Example 1: 运营端更新管控本地Topic元数据**

运营端更新管控本地Topic元数据成功

Input: 

```
tccli trocket ModifyTopicMetaInternal --cli-unfold-argument  \
    --InstanceId rmq-4k4orqgq \
    --Topic topic-498283 \
    --QueueNum 4 \
    --Remark test-remark \
    --TopicType FIFO
```

Output: 
```
{
    "Response": {
        "RequestId": "45bc44b4-432a-4b2d-b0ba-a63dcc34b480"
    }
}
```

