**Example 1: 关闭 DB Custom 节点**



Input: 

```
tccli dbdc StopDBCustomNodes --cli-unfold-argument  \
    --NodeIds dbcn-lqzvz9er \
    --StopType HARD
```

Output: 
```
{
    "Response": {
        "TaskId": 4072,
        "RequestId": "1288251d-7831-46ed-9a49-c1ea2c122767"
    }
}
```

