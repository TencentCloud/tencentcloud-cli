**Example 1: 资源实例绑定DDoS高级策略**



Input: 

```
tccli dayu ModifyResBindDDoSPolicy --cli-unfold-argument  \
    --Business bgpip \
    --Id bgpip-000000xe \
    --PolicyId policy-000000xe \
    --Method bind
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

