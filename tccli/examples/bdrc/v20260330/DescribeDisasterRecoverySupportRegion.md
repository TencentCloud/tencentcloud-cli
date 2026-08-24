**Example 1: 查询支持的地域**



Input: 

```
tccli bdrc DescribeDisasterRecoverySupportRegion --cli-unfold-argument  \
    --Status valid
```

Output: 
```
{
    "Response": {
        "SupportRegionSet": [
            {
                "SourceRegion": "ap-guangzhou",
                "Status": "valid",
                "SupportType": "REGION",
                "SupportZoneRules": []
            }
        ],
        "TotalCount": 1,
        "RequestId": "fafbc7ed-5129-4383-8c5b-b01af94d2661"
    }
}
```

