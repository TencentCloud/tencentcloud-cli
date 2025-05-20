**Example 1: 查询镜像跨账号共享信息**



Input: 

```
tccli lighthouse DescribeBlueprintsShareAcrossAccountInfos --cli-unfold-argument  \
    --BlueprintIds lhbp-6jc6l8yb
```

Output: 
```
{
    "Response": {
        "BlueprintShareAcrossAccountInfoSet": [
            {
                "BlueprintId": "lhbp-6jc6l8yb",
                "AccountId": "700000164995",
                "CreatedTime": "2023-09-13T00:29:12Z"
            }
        ],
        "TotalCount": 1,
        "RequestId": "d339efa9-f637-4ba9-a7c6-fb89ce67d76f"
    }
}
```

