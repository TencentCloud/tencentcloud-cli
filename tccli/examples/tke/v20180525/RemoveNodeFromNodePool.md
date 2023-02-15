**Example 1: 移出节点池节点**

移出节点池节点

Input: 

```
tccli tke RemoveNodeFromNodePool --cli-unfold-argument  \
    --ClusterId cls-hca1bmif \
    --NodePoolId np-5tx2jmn9 \
    --InstanceIds ins-74mbca66
```

Output: 
```
{
    "Response": {
        "RequestId": "1b9d6bcd-bbfd-4b2d-9b5d-ab8dfbbd4bed"
    }
}
```

