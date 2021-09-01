**Example 1: 修改DDoS高级策略**



Input: 

```
tccli dayu ModifyDDoSPolicy --cli-unfold-argument  \
    --Business bgpip \
    --PolicyId policy-000000xe \
    --DropOptions.0.DropTcp 0 \
    --DropOptions.0.DropUdp 0 \
    --DropOptions.0.DropIcmp 1 \
    --DropOptions.0.DropOther 1 \
    --DropOptions.0.DropAbroad 1 \
    --DropOptions.0.CheckSyncConn 1
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

