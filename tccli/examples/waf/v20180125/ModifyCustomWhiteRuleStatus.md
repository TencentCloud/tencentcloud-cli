**Example 1: 切换精准白名单规则的开关**



Input: 

```
tccli waf ModifyCustomWhiteRuleStatus --cli-unfold-argument  \
    --RuleId 1100000001 \
    --Domain waf.tencentcloudapi.com \
    --Status 1
```

Output: 
```
{
    "Response": {
        "RequestId": "5d207f4f-0d41-4f5d-bce2-0320090c98d8",
        "Success": {
            "Message": "Success",
            "Code": "Success"
        }
    }
}
```

