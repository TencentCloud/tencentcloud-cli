**Example 1: 查看超级节点列表**

查看超级节点列表

Input: 

```
tccli tke DescribeClusterVirtualNode --cli-unfold-argument  \
    --ClusterId cls-e55paxnt \
    --NodePoolId np-e55paxnt
```

Output: 
```
{
    "Response": {
        "RequestId": "1ac0d3ae-063e-4789-93fe-3c73e93191b9",
        "TotalCount": 1,
        "Nodes": [
            {
                "Name": "eklet-subnet-e55paxnt-0",
                "SubnetId": "subnet-e55paxnt",
                "Phase": "Running",
                "CreatedTime": "2023-10-15T14:30:00Z"
            }
        ]
    }
}
```

