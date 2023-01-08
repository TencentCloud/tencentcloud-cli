**Example 1: 创建虚拟节点**



Input: 

```
tccli tke CreateClusterVirtualNode --cli-unfold-argument  \
    --ClusterId cls-abcd1234 \
    --NodePoolId np-abcd1234 \
    --SubnetId subnet-abcd1234
```

Output: 
```
{
    "Response": {
        "RequestId": "1ac0d3ae-063e-4789-93fe-3c73e93191b9",
        "NodeName": "eklet-subnet-1234-0"
    }
}
```

