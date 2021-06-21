**Example 1: 解绑高防弹性公网IP**



Input: 

```
tccli antiddos DisassociateDDoSEipAddress --cli-unfold-argument  \
    --InstanceId bgpip-0000011x \
    --Eip 1.1.1.1
```

Output: 
```
{
    "Response": {
        "RequestId": "5063ab0a-a8a7-41e8-ace2-263b2c1c8794"
    }
}
```

