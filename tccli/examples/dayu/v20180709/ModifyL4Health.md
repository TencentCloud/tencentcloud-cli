**Example 1: 修改L4转发规则健康检查参数**



Input: 

```
tccli dayu ModifyL4Health --cli-unfold-argument  \
    --Business bgpip \
    --Id bgpip-000000xe \
    --Healths.0.RuleId rule-000000xe \
    --Healths.0.Enable 1 \
    --Healths.0.TimeOut 60 \
    --Healths.0.Interval 300 \
    --Healths.0.KickNum 3 \
    --Healths.0.AliveNum 3
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

