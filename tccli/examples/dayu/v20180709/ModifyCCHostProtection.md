**Example 1: 开启或关闭CC域名防护**



Input: 

```
tccli dayu ModifyCCHostProtection --cli-unfold-argument  \
    --Business bgpip \
    --Id bgpip-000000xe \
    --RuleId rule-00000002 \
    --Method open
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

