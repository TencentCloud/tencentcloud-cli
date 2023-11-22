**Example 1: 获取 WAF 防护域名**

获取 WAF 防护域名

Input: 

```
tccli tse DescribeWafDomains --cli-unfold-argument  \
    --GatewayId gateway-0f7c158e
```

Output: 
```
{
    "Response": {
        "Result": {
            "Domains": [
                "example.com"
            ]
        },
        "RequestId": "741e4e82-371d-48de-a843-867c69ff114d"
    }
}
```

