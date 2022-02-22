**Example 1: 修改DDoS黑白名单列表**



Input: 

```
tccli antiddos ModifyDDoSBlackWhiteIpList --cli-unfold-argument  \
    --InstanceId bgpip-00023423 \
    --OldIpType black \
    --OldIp.Ip 1.1.1.1 \
    --OldIp.Mask 0 \
    --NewIpType black \
    --NewIp.Ip 1.1.1.2 \
    --NewIp.Mask 0
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

