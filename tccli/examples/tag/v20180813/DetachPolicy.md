**Example 1: 从目标节点解绑标签策略**

从目标节点解绑标签策略

Input: 

```
tccli tag DetachPolicy --cli-unfold-argument  \
    --TargetId 100000548134 \
    --PolicyId 10004
```

Output: 
```
{
    "Response": {
        "RequestId": "37198911-6131-4754-adfb-71a187637ce8"
    }
}
```

