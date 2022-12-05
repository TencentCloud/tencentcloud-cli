**Example 1: 删除DDoS防护的特征过滤规则**



Input: 

```
tccli antiddos DeletePacketFilterConfig --cli-unfold-argument  \
    --InstanceId bgpip-111111q1 \
    --PacketFilterConfig.MatchType2  \
    --PacketFilterConfig.MatchBegin2 no_match \
    --PacketFilterConfig.Str2  \
    --PacketFilterConfig.SportEnd 0 \
    --PacketFilterConfig.IsNot 0 \
    --PacketFilterConfig.PktlenMax 0 \
    --PacketFilterConfig.MatchLogic none \
    --PacketFilterConfig.MatchBegin begin_l4 \
    --PacketFilterConfig.Offset 0 \
    --PacketFilterConfig.SportStart 0 \
    --PacketFilterConfig.DportStart 0 \
    --PacketFilterConfig.PktlenMin 0 \
    --PacketFilterConfig.IsNot2 0 \
    --PacketFilterConfig.Depth 0 \
    --PacketFilterConfig.Str \x3908 \
    --PacketFilterConfig.Action drop \
    --PacketFilterConfig.Protocol all \
    --PacketFilterConfig.MatchType sunday \
    --PacketFilterConfig.DportEnd 0 \
    --PacketFilterConfig.Offset2 0 \
    --PacketFilterConfig.Depth2 0 \
    --PacketFilterConfig.Id 01j9d4hi
```

Output: 
```
{
    "Response": {
        "RequestId": "5063ab0a-a8a7-41e8-ace2-263b2c1c8794"
    }
}
```

