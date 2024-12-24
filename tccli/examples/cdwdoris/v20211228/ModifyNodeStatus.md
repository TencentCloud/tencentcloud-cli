**Example 1: 调整节点状态**

调整节点状态

Input: 

```
tccli cdwdoris ModifyNodeStatus --cli-unfold-argument  \
    --InstanceId 11 \
    --NodeInfos.0.Status 0 \
    --NodeInfos.0.Ip 11 \
    --NodeInfos.0.NodeRole 11 \
    --NodeInfos.0.NodeName 11 \
    --OperationCode 11
```

Output: 
```
{
    "Response": {
        "RequestId": "xxx-12",
        "FlowId": 0,
        "ErrorMsg": ""
    }
}
```

