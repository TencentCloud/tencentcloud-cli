**Example 1: 删除CC四层黑白名单**



Input: 

```
tccli antiddos DeleteCcBlackWhiteIpList --cli-unfold-argument  \
    --InstanceId bgpip-111111qq \
    --PolicyId ccBlackWhite-000000s0
```

Output: 
```
{
    "Response": {
        "RequestId": "5063ab0a-a8a7-41e8-ace2-263b2c1c8794"
    }
}
```

