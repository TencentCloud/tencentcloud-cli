**Example 1: 转发地域列表查询接口**



Input: 

```
tccli monitor DescribeDispenseRegion --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RegionList": [
            {
                "Region": "gz",
                "RegionCnName": "广州",
                "RegionEnName": "ap-guangzhou",
                "RuleNumber": 4
            },
            {
                "Region": "sheec",
                "RegionCnName": "沈阳EC",
                "RegionEnName": "ap-shenyang-ec",
                "RuleNumber": 0
            }
        ],
        "RequestId": "a4236754-668e-4b89-9b25-4b02d380297f"
    }
}
```

