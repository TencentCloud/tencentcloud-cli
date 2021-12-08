**Example 1: 镜像仓库查询镜像高危行为列表**



Input: 

```
tccli tcss DescribeAssetImageRegistryRiskInfoList --cli-unfold-argument  \
    --Filters.0.ExactMatch False \
    --Filters.0.Name Level \
    --Filters.0.Values all \
    --Filters.1.ExactMatch False \
    --Filters.1.Name Behavior \
    --Filters.1.Values all \
    --Filters.2.ExactMatch False \
    --Filters.2.Name Type \
    --Filters.2.Values all \
    --Id 6947411 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "c283b995-d932-436d-8deb-11d2b7eb216c",
        "List": [],
        "TotalCount": 0
    }
}
```

