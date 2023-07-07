**Example 1: 修改虚拟节点池**

修改虚拟节点池

Input: 

```
tccli tke ModifyClusterVirtualNodePool --cli-unfold-argument  \
    --ClusterId cls-abcd1234 \
    --NodePoolId np-abcd1234 \
    --Name virtual-node-prod
```

Output: 
```
{
    "Response": {
        "RequestId": "1ac0d3ae-063e-4789-93fe-3c73e93191b9"
    }
}
```

