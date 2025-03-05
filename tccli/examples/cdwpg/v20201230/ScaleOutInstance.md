**Example 1: ScaleOutInstance**



Input: 

```
tccli cdwpg ScaleOutInstance --cli-unfold-argument  \
    --InstanceId abc \
    --NodeType dn \
    --ScaleOutCount 2
```

Output: 
```
{
    "Response": {
        "FlowId": "abc",
        "ErrorMsg": "abc",
        "RequestId": "abc"
    }
}
```

