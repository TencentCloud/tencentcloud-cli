**Example 1: 枚举地域**



Input: 

```
tccli ckafka DescribeRegion --cli-unfold-argument  \
    --Business 10
```

Output: 
```
{
    "Response": {
        "RequestId": "4b44eaee-3807-482d-a589-9f0126615d9d",
        "Result": [
            {
                "AreaName": "华南地区",
                "Ipv6": 0,
                "MultiZone": 1,
                "RegionCode": "gz",
                "RegionCodeV3": "ap-guangzhou",
                "RegionId": 1,
                "RegionName": "广州",
                "Support": "profession,serverless"
            }
        ]
    }
}
```

