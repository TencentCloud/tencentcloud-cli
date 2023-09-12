**Example 1: 创建主题**

创建主题

Input: 

```
tccli trocket CreateTopic --cli-unfold-argument  \
    --InstanceId rmq-72mo3a9o \
    --Topic test \
    --TopicType NORMAL \
    --QueueNum 16 \
    --Remark remoark
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "InstanceId": "rmq-72mo3a9o",
        "RequestId": "97f45511-b653-4e2a-ade6-58c8d3ae523b",
        "Topic": "test"
    }
}
```

