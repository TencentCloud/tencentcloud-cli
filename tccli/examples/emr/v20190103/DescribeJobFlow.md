**Example 1: 查询任务流程**



Input: 

```
tccli emr DescribeJobFlow --cli-unfold-argument  \
    --JobFlowId 1
```

Output: 
```
{
    "Response": {
        "State": "JobFlowFinish",
        "Details": [],
        "RequestId": "5a96d30f-a251-42a0-82e2-f85325f5b89b"
    }
}
```

