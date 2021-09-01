**Example 1: 清空队列中堆积的消息**

清空队列中堆积的消息

Input: 

```
tccli cmq ClearQueue --cli-unfold-argument  \
    --QueueName test
```

Output: 
```
{
    "Response": {
        "RequestId": "3e0dff9d-9ed5-47c3-beb2-a42c1d69e1cc"
    }
}
```

