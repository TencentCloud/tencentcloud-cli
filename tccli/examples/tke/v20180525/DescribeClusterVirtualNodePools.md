**Example 1: 查看虚拟节点池列表**



Input: 

```
tccli tke DescribeClusterVirtualNodePools --cli-unfold-argument  \
    --ClusterId cls-abcd1234
```

Output: 
```
{
    "Response": {
        "RequestId": "1ac0d3ae-063e-4789-93fe-3c73e93191b9",
        "NodePoolSet": [
            {
                "NodePoolId": "np-abcd1234",
                "SubnetIds": [
                    "subnet-abcd1234"
                ],
                "Name": "virtual-nodepool",
                "LifeState": "normal"
            }
        ],
        "TotalCount": 1
    }
}
```

