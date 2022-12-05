**Example 1: 修改CC四层黑白名单**



Input: 

```
tccli antiddos ModifyCcBlackWhiteIpList --cli-unfold-argument  \
    --InstanceId bgpip-111111q1 \
    --IpList.0.Ip 1.1.1.1 \
    --IpList.0.Mask 1 \
    --Type black \
    --PolicyId ccBlackWhite-00000312
```

Output: 
```
{
    "Response": {
        "RequestId": "5063ab0a-a8a7-41e8-ace2-263b2c1c8794"
    }
}
```

