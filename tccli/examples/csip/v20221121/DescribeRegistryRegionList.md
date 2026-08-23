**Example 1: 查询镜像仓库地域列表**



Input: 

```
tccli csip DescribeRegistryRegionList --cli-unfold-argument  \
    --MemberId mem-12e1se11
```

Output: 
```
{
    "Response": {
        "DefaultRegion": "ap-guangzhou",
        "Regions": [
            {
                "Region": "ap-guangzhou",
                "RegionCode": "gz",
                "RegionId": 1,
                "RegionName": "华南地区（广州）",
                "RegionNameEn": "South China (Guangzhou)"
            }
        ],
        "RequestId": "d7145fdb-8d92-4343-8c27-b482f63fb06a"
    }
}
```

