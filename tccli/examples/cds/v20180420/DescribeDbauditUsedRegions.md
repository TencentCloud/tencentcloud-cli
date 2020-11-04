**Example 1: 查询可售卖地域列表**



Input: 

```
tccli cds DescribeDbauditUsedRegions --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7",
        "RegionSet": [
            {
                "Region": "ap-guangzhou",
                "RegionName": "广州",
                "RegionId": "1",
                "RegionState": 1
            },
            {
                "Region": "ap-shanghai",
                "RegionName": "上海",
                "RegionId": 4,
                "RegionState": 1
            }
        ]
    }
}
```

