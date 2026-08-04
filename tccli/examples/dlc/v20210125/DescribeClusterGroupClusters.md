**Example 1: 查询计算组关联 cluster 列表**



Input: 

```
tccli dlc DescribeClusterGroupClusters --cli-unfold-argument  \
    --Id rayclustergroup-tfe719-rm1q \
    --SampleLimit 10 \
    --Status running
```

Output: 
```
{
    "Response": {
        "Count": 0,
        "SampleClusters": [],
        "RequestId": "5720b553-2caf-4ee4-a224-158dc518dedb"
    }
}
```

