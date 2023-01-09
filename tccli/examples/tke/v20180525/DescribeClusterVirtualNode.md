**Example 1: 查看虚拟节点列表**



Input: 

```
tccli tke DescribeClusterVirtualNode --cli-unfold-argument  \
    --ClusterId cls-abcd1234 \
    --NodePoolId np-abcd1234
```

Output: 
```
{
    "Response": {
        "RequestId": "1ac0d3ae-063e-4789-93fe-3c73e93191b9",
        "TotalCount": 1,
        "Nodes": [
            {
                "Name": "eklet-subnet-abcd1234-0",
                "SubnetId": "subnet-abcd1234",
                "Phase": "Running"
            }
        ]
    }
}
```

