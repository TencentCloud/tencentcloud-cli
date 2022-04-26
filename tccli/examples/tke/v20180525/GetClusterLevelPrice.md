**Example 1: 获取集群规模价格**



Input: 

```
tccli tke GetClusterLevelPrice --cli-unfold-argument  \
    --ClusterLevel 3600
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "Cost": 6,
        "TotalCost": 6
    }
}
```

