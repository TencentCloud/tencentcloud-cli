**Example 1: 创建队列**

创建队列

Input: 

```
tccli tdmq CreateCmqQueue --cli-unfold-argument  \
    --QueueName test
```

Output: 
```
{
    "Response": {
        "QueueId": "queue-ges05csc",
        "RequestId": "3e0dff9d-9ed5-47c3-beb2-a42c1d69e1cc"
    }
}
```

**Example 2: 示例**

创建队列

Input: 

```
tccli tdmq CreateCmqQueue --cli-unfold-argument  \
    --QueueName test789
```

Output: 
```
{
    "Response": {
        "RequestId": "864b1295-ed7e-45ed-9602-be53ac23177b",
        "QueueId": "cmqq-rd42drdeaag9"
    }
}
```

