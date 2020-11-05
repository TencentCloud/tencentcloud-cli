**Example 1: Binding advanced DDoS policy to resource instance**



Input: 

```
tccli dayu ModifyResBindDDoSPolicy --cli-unfold-argument  \
    --Business bgpip\
    --Id bgpip-000000xe\
    --PolicyId policy-000000xe\
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

