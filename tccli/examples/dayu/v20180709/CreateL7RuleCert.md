**Example 1: 配置L7转发规则的证书**



Input: 

```
tccli dayu CreateL7RuleCert --cli-unfold-argument  \
    --Business bgpip \
    --Id bgpip-000000xe \
    --RuleId rule-00000001 \
    --CertType 2 \
    --SSLId sslid123
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "Success": {
            "Code": "Success",
            "Message": "Success"
        }
    }
}
```

