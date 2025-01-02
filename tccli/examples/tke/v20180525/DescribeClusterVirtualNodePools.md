**Example 1: 查看超级节点池列表**

查看超级节点池列表

Input: 

```
tccli tke DescribeClusterVirtualNodePools --cli-unfold-argument  \
    --ClusterId cls-e55paxnt
```

Output: 
```
{
    "Response": {
        "RequestId": "1ac0d3ae-063e-4789-93fe-3c73e93191b9",
        "NodePoolSet": [
            {
                "NodePoolId": "np-e55paxnt",
                "SubnetIds": [
                    "subnet-e55paxnt"
                ],
                "Name": "virtual-nodepool",
                "LifeState": "normal",
                "Labels": [],
                "Taints": []
            }
        ],
        "TotalCount": 1
    }
}
```

