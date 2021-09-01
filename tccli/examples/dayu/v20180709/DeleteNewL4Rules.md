**Example 1: 删除L4转发规则**



Input: 

```
tccli dayu DeleteNewL4Rules --cli-unfold-argument  \
    --Business bgpip \
    --Rule.0.Id bgpip-000001 \
    --Rule.0.Ip 192.168.1.1 \
    --Rule.0.RuleIdList rule-000002uq
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

