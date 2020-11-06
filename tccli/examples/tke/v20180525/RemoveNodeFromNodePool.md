**Example 1: 移出节点池节点**



Input: 

```
tccli tke RemoveNodeFromNodePool --cli-unfold-argument  \
    --ClusterId cls-xxxxxx \
    --NodePoolId np-xxxxxxxx \
    --InstanceIds ins-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "xxxxxx"
    }
}
```

