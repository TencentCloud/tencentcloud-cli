**Example 1: 删除队列**

从集群删除指定队列。

Input: 

```
tccli thpc DeleteQueue --cli-unfold-argument  \
    --ClusterId hpc-prkxbd7c \
    --QueueName compute
```

Output: 
```
{
    "Response": {
        "RequestId": "13ee84a5-7846-4682-8877-1c8f94962d10"
    }
}
```

