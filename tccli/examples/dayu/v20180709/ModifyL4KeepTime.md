**Example 1: 修改L4转发规则的会话保持**



Input: 

```
tccli dayu ModifyL4KeepTime --cli-unfold-argument  \
    --Business bgpip \
    --Id bgpip-000000xe \
    --RuleId rule-000000xe \
    --KeepEnable 1 \
    --KeepTime 300
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

