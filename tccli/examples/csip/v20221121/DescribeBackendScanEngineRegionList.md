**Example 1: 查询后台扫描引擎地域列表**



Input: 

```
tccli csip DescribeBackendScanEngineRegionList --cli-unfold-argument  \
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
        "RequestId": "2e27016b-46b6-4243-b548-298180f20c49"
    }
}
```

