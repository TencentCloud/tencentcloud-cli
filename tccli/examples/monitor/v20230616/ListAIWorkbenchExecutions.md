**Example 1: test**



Input: 

```
tccli monitor ListAIWorkbenchExecutions --cli-unfold-argument  \
    --AgentId agt-******** \
    --ExecutionIds exe-************ \
    --TaskIds tsk-********
```

Output: 
```
{
    "Response": {
        "Executions": [],
        "PageResult": {
            "CurrentPageNo": 0,
            "TotalCount": 0,
            "TotalPage": 0
        },
        "RequestId": "d3445330-9348-41f9-9713-36a2f336ba26"
    }
}
```

