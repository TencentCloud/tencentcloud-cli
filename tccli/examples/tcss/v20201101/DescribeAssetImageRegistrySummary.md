**Example 1: 镜像仓库查询镜像统计信息**



Input: 

```
tccli tcss DescribeAssetImageRegistrySummary --cli-unfold-argument  \
    --Filters.0.Name OnlyShowLatest \
    --Filters.0.ExactMatch True \
    --Filters.0.Values 1021
```

Output: 
```
{
    "Response": {
        "RequestId": "84bdc033-18ce-443a-9d61-8d5a099e6063",
        "UnScannedImageCnt": 2
    }
}
```

