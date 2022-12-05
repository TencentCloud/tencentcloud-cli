**Example 1: 修改DDoS防护的特征过滤规则**



Input: 

```
tccli antiddos ModifyPacketFilterConfig --cli-unfold-argument  \
    --InstanceId bgpip-00000001 \
    --PacketFilterConfig.Action drop_rst \
    --PacketFilterConfig.Depth 4 \
    --PacketFilterConfig.Depth2 4 \
    --PacketFilterConfig.DportEnd 8101 \
    --PacketFilterConfig.DportStart 8101 \
    --PacketFilterConfig.Id 0176fm61 \
    --PacketFilterConfig.IsNot 0 \
    --PacketFilterConfig.IsNot2 0 \
    --PacketFilterConfig.MatchBegin begin_l4 \
    --PacketFilterConfig.MatchBegin2 begin_l4 \
    --PacketFilterConfig.MatchLogic and \
    --PacketFilterConfig.MatchType sunday \
    --PacketFilterConfig.MatchType2 pcre \
    --PacketFilterConfig.Offset 14 \
    --PacketFilterConfig.Offset2 14 \
    --PacketFilterConfig.PktlenMax 100 \
    --PacketFilterConfig.PktlenMin 1 \
    --PacketFilterConfig.Protocol tcp \
    --PacketFilterConfig.SportEnd 65535 \
    --PacketFilterConfig.SportStart 1 \
    --PacketFilterConfig.Str \x3908 \
    --PacketFilterConfig.Str2 \xfaf0
```

Output: 
```
{
    "Response": {
        "RequestId": "5063ab0a-a8a7-41e8-ace2-263b2c1c8794"
    }
}
```

