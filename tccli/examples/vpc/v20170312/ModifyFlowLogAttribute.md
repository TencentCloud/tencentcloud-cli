**Example 1: 修改流日志属性**

修改流日志属性

Input: 

```
tccli vpc ModifyFlowLogAttribute --cli-unfold-argument  \
    --FlowLogId fl-xxxxxx \
    --FlowLogName xxxxx \
    --VpcId vpc-xxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "404428db-f850-40c2-803d-0aae49aba43a"
    }
}
```

