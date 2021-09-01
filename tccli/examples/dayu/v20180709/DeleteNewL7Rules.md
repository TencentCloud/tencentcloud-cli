**Example 1: 删除L7转发规则**



Input: 

```
tccli dayu DeleteNewL7Rules --cli-unfold-argument  \
    --Business bgpip \
    --Rule.0.Id bgpip-0000001 \
    --Rule.0.Ip 11.11.11.11 \
    --Rule.0.RuleIdList rule-000004qq
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

