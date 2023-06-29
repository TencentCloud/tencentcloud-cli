**Example 1: 镜像仓库查询镜像漏洞列表**



Input: 

```
tccli tcss DescribeAssetImageRegistryVulList --cli-unfold-argument  \
    --Filters.0.ExactMatch False \
    --Filters.0.Name Level \
    --Filters.0.Values all \
    --Filters.1.ExactMatch False \
    --Filters.1.Name Tag \
    --Filters.1.Values all \
    --Id 1929935 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "4ffca7b7-3d73-4317-8a76-a2b00e90f3b2",
        "List": [],
        "TotalCount": 0
    }
}
```

