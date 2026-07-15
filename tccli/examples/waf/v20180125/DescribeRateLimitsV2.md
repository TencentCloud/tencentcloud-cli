**Example 1: DescribeLimitRules**



Input: 

```
tccli waf DescribeRateLimitsV2 --cli-unfold-argument  \
    --Domain www.test.com \
    --Id 0 \
    --Name testname \
    --Method  \
    --LimitObject API \
    --Status 0 \
    --Order desc \
    --By  \
    --Offset 0 \
    --Limit 10 \
    --Filters.0.Name status \
    --Filters.0.Values 0 \
    --Filters.0.ExactMatch True
```

Output: 
```
{
    "Response": {
        "Total": 0,
        "BaseInfo": {
            "Code": 1,
            "Info": "success"
        },
        "RateLimits": [
            {
                "LimitRuleID": 400000023,
                "Name": "testname",
                "Priority": 50,
                "Status": 0,
                "TsVersion": 0,
                "LimitObject": "API",
                "LimitMethod": {
                    "Method": "GET",
                    "Type": "EXACT"
                },
                "LimitPaths": {
                    "Path": "/url",
                    "Type": "EXACT"
                },
                "LimitHeaders": [
                    {
                        "Key": "",
                        "Value": "v1,v2",
                        "Type": "IN"
                    }
                ],
                "LimitWindow": {
                    "Second": 0,
                    "Minute": 10
                },
                "LimitStrategy": 0,
                "LimitHeaderName": {}
            }
        ],
        "RequestId": "546b2091-1a59-4bd9-818d-47ab565102d9"
    }
}
```

