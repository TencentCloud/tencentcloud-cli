**Example 1: 新建 WAF 防护域名**

新建 WAF 防护域名

Input: 

```
tccli tse CreateWafDomains --cli-unfold-argument  \
    --GatewayId gateway-0f7c158e \
    --Domains example.com
```

Output: 
```
{
    "Response": {
        "RequestId": "741e4e82-371d-48de-a843-867c69ff114d"
    }
}
```

