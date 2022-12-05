**Example 1: 证书绑定域名列表**



Input: 

```
tccli antiddos CreateL7RuleCerts --cli-unfold-argument  \
    --CertId cMgC0TpV \
    --L7Rules.0.InsId bgpip-000001eo \
    --L7Rules.0.AppId 251008915 \
    --L7Rules.0.Protocol https \
    --L7Rules.0.Domain www.test.com \
    --L7Rules.0.VirtualPort 443 \
    --L7Rules.0.SSLId  \
    --L7Rules.0.Status 8
```

Output: 
```
{
    "Response": {
        "RequestId": "a7d078cc-2547-47f8-b1d6-65bc67d28ae7",
        "Success": {
            "Code": "Success",
            "Message": "Success"
        }
    }
}
```

