**Example 1: 获取TKE集群列表**



Input: 

```
tccli wedata DescribeInLongTkeClusterList --cli-unfold-argument  \
    --Status Running \
    --PageIndex 1 \
    --PageSize 1 \
    --ClusterName  \
    --ProjectId 1 \
    --HasAgent True \
    --ClusterType  \
    --TkeRegion ap-beijing
```

Output: 
```
{
    "Response": {
        "PageIndex": 1,
        "PageSize": 1,
        "Items": [
            {
                "Status": "Running",
                "VpcId": "vpc-awed345",
                "TkeRegion": "ap-beijing",
                "ClusterName": "cls-test",
                "HasAgent": true,
                "ClusterId": "cls-0u7ofrsl",
                "ClusterType": "INDEPENDENT_CLUSTER",
                "AgentId": "16878689876877778"
            }
        ],
        "TotalPage": 1,
        "TotalCount": 1,
        "RequestId": "89add-786986"
    }
}
```

