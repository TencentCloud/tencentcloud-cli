**Example 1: 设置DDoS防护的协议封禁配置**



Input: 

```
tccli antiddos CreateProtocolBlockConfig --cli-unfold-argument  \
    --InstanceId bgpip-0000011x \
    --ProtocolBlockConfig.DropTcp 1 \
    --ProtocolBlockConfig.DropUdp 1 \
    --ProtocolBlockConfig.DropIcmp 1 \
    --ProtocolBlockConfig.DropOther 1 \
    --ProtocolBlockConfig.CheckExceptNullConnect 1
```

Output: 
```
{
    "Response": {
        "RequestId": "5063ab0a-a8a7-41e8-ace2-263b2c1c8794"
    }
}
```

