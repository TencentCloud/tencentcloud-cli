**Example 1: 查询队列弹性伸缩配置**



Input: 

```
tccli thpc DescribeQueueAutoScaling --cli-unfold-argument  \
    --ClusterId hpc-d9ng14l3 \
    --QueueName lurka-auto-as
```

Output: 
```
{
    "Response": {
        "RequestId": "539a36cc-f30c-4e2b-8f4f-f56a6b2ca141"
    }
}
```

