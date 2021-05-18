**Example 1: 修改队列属性**



Input: 

```
tccli tdmq ModifyCmqQueueAttribute --cli-unfold-argument  \
    --QueueName test \
    --MaxMsgSize 1024
```

Output: 
```
{
    "Response": {
        "RequestId": "3e0dff9d-9ed5-47c3-beb2-a42c1d69e1cc"
    }
}
```

