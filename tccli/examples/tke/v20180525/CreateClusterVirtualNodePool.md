**Example 1: 创建超级节点池**

创建超级节点池

Input: 

```
tccli tke CreateClusterVirtualNodePool --cli-unfold-argument  \
    --ClusterId cls-e55paxnt \
    --Name vk-nodepoll \
    --SubnetIds subnet-e55paxnt \
    --SecurityGroupIds sg-e55paxnt
```

Output: 
```
{
    "Response": {
        "NodePoolId": "np-e55paxnt",
        "RequestId": "1ac0d3ae-063e-4789-93fe-3c73e93191b9"
    }
}
```

