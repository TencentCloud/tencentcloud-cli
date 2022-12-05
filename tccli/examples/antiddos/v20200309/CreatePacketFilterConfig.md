**Example 1: 添加DDoS防护的特征过滤规则**



Input: 

```
tccli antiddos CreatePacketFilterConfig --cli-unfold-argument  \
    --InstanceId bgpip-000002q2 \
    --PacketFilterConfig.Action drop_rst \
    --PacketFilterConfig.Depth 4 \
    --PacketFilterConfig.DportEnd 18373 \
    --PacketFilterConfig.DportStart 18373 \
    --PacketFilterConfig.IsNot 0 \
    --PacketFilterConfig.MatchBegin begin_l4 \
    --PacketFilterConfig.MatchType sunday \
    --PacketFilterConfig.Offset 14 \
    --PacketFilterConfig.PktlenMax 100 \
    --PacketFilterConfig.PktlenMin 1 \
    --PacketFilterConfig.Protocol tcp \
    --PacketFilterConfig.SportEnd 65535 \
    --PacketFilterConfig.SportStart 1 \
    --PacketFilterConfig.Str \x05ac
```

Output: 
```
{
    "Response": {
        "RequestId": "5063ab0a-a8a7-41e8-ace2-263b2c1c8794"
    }
}
```

