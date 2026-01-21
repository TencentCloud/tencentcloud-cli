**Example 1: 切换队列**

用于同集群下队列切换

Input: 

```
tccli thpc ModifyNodeAttribute --cli-unfold-argument  \
    --NodeId node-qkpdhp90 \
    --QueueName usr_queue
```

Output: 
```
{
    "Response": {
        "RequestId": "8c16f5ef-f532-4574-a4d2-7cee0c38acb8"
    }
}
```

**Example 2: 隔离节点**

手动隔离节点，修改节点的资源使用为隔离状态，阻止作业调度到目标节点

Input: 

```
tccli thpc ModifyNodeAttribute --cli-unfold-argument  \
    --NodeId node-xxx \
    --NodeAllocateState ISOLATE
```

Output: 
```
{
    "Response": {
        "RequestId": "e55f6797-8672-435a-875a-8f05d9b3fadaaa"
    }
}
```

