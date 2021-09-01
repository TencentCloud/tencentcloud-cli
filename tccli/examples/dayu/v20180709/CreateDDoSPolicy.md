**Example 1: 添加DDoS高级策略**



Input: 

```
tccli dayu CreateDDoSPolicy --cli-unfold-argument  \
    --Business bgpip \
    --Name testpolicy \
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
        "PolicyId": "policy-000003h7",
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

