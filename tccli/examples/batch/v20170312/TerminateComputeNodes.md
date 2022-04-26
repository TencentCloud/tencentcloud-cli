**Example 1: 批量销毁计算节点**



Input: 

```
tccli batch TerminateComputeNodes --cli-unfold-argument  \
    --EnvId env-lcx7qbbr \
    --ComputeNodeIds node-lcpcej85 node-lcz8jkvw
```

Output: 
```
{
    "Response": {
        "RequestId": "c50bfbf1-d214-4e41-90f6-39270dc9f071"
    }
}
```

