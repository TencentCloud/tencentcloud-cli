**Example 1: 创建按量计费超级节点**

创建按量计费超级节点

Input: 

```
tccli tke CreateClusterVirtualNode --cli-unfold-argument  \
    --ClusterId cls-e55paxnt \
    --NodePoolId np-e55paxnt \
    --SubnetId subnet-e55paxnt
```

Output: 
```
{
    "Response": {
        "RequestId": "1ac0d3ae-063e-4789-93fe-3c73e93191b9",
        "NodeName": "eklet-subnet-qbc3zefo-0"
    }
}
```

