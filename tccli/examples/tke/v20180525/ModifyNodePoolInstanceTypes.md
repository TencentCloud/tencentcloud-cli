**Example 1: 修改节点池机型**



Input: 

```
tccli tke ModifyNodePoolInstanceTypes --cli-unfold-argument  \
    --ClusterId cls-xxx \
    --NodePoolId np-xxx \
    --InstanceTypes ins-xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "xxxxxxxx"
    }
}
```

