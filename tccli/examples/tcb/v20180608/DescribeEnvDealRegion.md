**Example 1: 续费环境查询下单地域**

续费环境查询下单地域 

Input: 

```
tccli tcb DescribeEnvDealRegion --cli-unfold-argument  \
    --EnvId test-12323 \
    --DealType ENV_POSTPAY \
    --DealAction RENEW \
    --DealRegion ap-shanghai
```

Output: 
```
{
    "Response": {
        "RequestId": "3e22b381-93a3-44c4-85b7-456679a7b8cd",
        "Region": "ap-shanghai",
        "Zone": "ap-shanghai-1",
        "RegionId": 4,
        "ZoneId": 200001
    }
}
```

