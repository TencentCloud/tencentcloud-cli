**Example 1: 创建虚拟节点池**

创建虚拟节点池

Input: 

```
tccli tke CreateClusterVirtualNodePool --cli-unfold-argument  \
    --ClusterId cls-abcd1234 \
    --Name vk-nodepoll \
    --SubnetIds subnet-abcd1234 \
    --SecurityGroupIds sg-abcd1234
```

Output: 
```
{
    "Response": {
        "NodePoolId": "np-abcd1234",
        "RequestId": "1ac0d3ae-063e-4789-93fe-3c73e93191b9"
    }
}
```

