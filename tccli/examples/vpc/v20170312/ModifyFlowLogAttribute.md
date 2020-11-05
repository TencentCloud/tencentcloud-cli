**Example 1: Modifying the attributes of a flow log**



Input: 

```
tccli vpc ModifyFlowLogAttribute --cli-unfold-argument  \
    --FlowLogId fl-xxxxxx\
    --FlowLogName xxxxx\
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

