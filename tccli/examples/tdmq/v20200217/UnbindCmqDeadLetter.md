**Example 1: 解绑死信队列**



Input: 

```
tccli tdmq UnbindCmqDeadLetter --cli-unfold-argument  \
    --SourceQueueName test
```

Output: 
```
{
    "Response": {
        "RequestId": "3e0dff9d-9ed5-47c3-beb2-a42c1d69e1cc"
    }
}
```

