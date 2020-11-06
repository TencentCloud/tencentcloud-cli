**Example 1: 修改DDoS高级策略名称**



Input: 

```
tccli dayu ModifyDDoSPolicyName --cli-unfold-argument  \
    --Business bgpip \
    --PolicyId policy-000000xe \
    --Name test
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

