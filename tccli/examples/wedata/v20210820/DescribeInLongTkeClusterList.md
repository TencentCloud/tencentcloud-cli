**Example 1: 获取TKE集群列表**



Input: 

```
tccli wedata DescribeInLongTkeClusterList --cli-unfold-argument  \
    --Status xx \
    --PageIndex 1 \
    --PageSize 1 \
    --ClusterName xx \
    --ProjectId xx \
    --HasAgent True \
    --ClusterType xx \
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
                "Status": "xx",
                "VpcId": "xx",
                "TkeRegion": "xx",
                "ClusterName": "xx",
                "HasAgent": true,
                "ClusterId": "xx",
                "ClusterType": "xx",
                "AgentId": "xx"
            }
        ],
        "TotalPage": 1,
        "TotalCount": 1,
        "RequestId": "xx"
    }
}
```

