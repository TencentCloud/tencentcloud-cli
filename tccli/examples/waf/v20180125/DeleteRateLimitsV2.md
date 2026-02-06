**Example 1: 删除限流规则**



Input: 

```
tccli waf DeleteRateLimitsV2 --cli-unfold-argument  \
    --Domain www.test.com \
    --LimitRuleIds 4000003024 4000003023
```

Output: 
```
{
    "Response": {
        "BaseInfo": {
            "Code": 0,
            "Info": "success"
        },
        "RequestId": "546b2091-1a59-4bd9-818d-47ab565102d9"
    }
}
```

