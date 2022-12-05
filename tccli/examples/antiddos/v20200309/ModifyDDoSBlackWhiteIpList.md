**Example 1: 修改DDoS黑白名单列表**



Input: 

```
tccli antiddos ModifyDDoSBlackWhiteIpList --cli-unfold-argument  \
    --InstanceId bgpip-00023423 \
    --OldIp.Ip 1.1.1.1 \
    --OldIp.Mask 0 \
    --NewIp.Ip 1.1.1.2 \
    --NewIp.Mask 0 \
    --NewIpType black \
    --OldIpType black
```

Output: 
```
{
    "Response": {
        "RequestId": "63591603-c943-46eb-9b78-c5498072291a"
    }
}
```

