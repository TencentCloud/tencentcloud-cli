**Example 1: 拉取函数异步事件列表**



Input: 

```
tccli scf ListAsyncEvents --cli-unfold-argument  \
    --FunctionName test \
    --Qualifier 1 \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "EventList": [],
        "RequestId": "26c5f1a9-ebd4-407e-83d7-ae8001cca644"
    }
}
```

