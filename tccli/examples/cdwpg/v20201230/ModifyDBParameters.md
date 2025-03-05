**Example 1: 1**



Input: 

```
tccli cdwpg ModifyDBParameters --cli-unfold-argument  \
    --InstanceId cdwpg-abc \
    --NodeConfigParams.0.NodeType dn \
    --NodeConfigParams.0.ConfigParams.0.ParameterName k1 \
    --NodeConfigParams.0.ConfigParams.0.ParameterValue v1 \
    --NodeConfigParams.0.ConfigParams.0.ParameterOldValue v0
```

Output: 
```
{
    "Response": {
        "TaskId": 0,
        "RequestId": "abddc"
    }
}
```

