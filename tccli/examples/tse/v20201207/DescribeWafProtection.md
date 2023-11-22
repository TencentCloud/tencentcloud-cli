**Example 1: 获取 WAF 防护状态**

获取 WAF 防护状态

Input: 

```
tccli tse DescribeWafProtection --cli-unfold-argument  \
    --GatewayId gateway-0f7c158e \
    --Type Global
```

Output: 
```
{
    "Response": {
        "Result": {
            "GlobalStatus": "Open"
        },
        "RequestId": "abc"
    }
}
```

