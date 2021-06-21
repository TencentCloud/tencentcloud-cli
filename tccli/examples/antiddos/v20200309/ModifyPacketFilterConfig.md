**Example 1: 修改DDoS防护的特征过滤规则**



Input: 

```
tccli antiddos ModifyPacketFilterConfig --cli-unfold-argument  \
    --InstanceId xx \
    --PacketFilterConfig.MatchType2 xx \
    --PacketFilterConfig.MatchBegin2 xx \
    --PacketFilterConfig.Str2 xx \
    --PacketFilterConfig.SportEnd 0 \
    --PacketFilterConfig.IsNot 0 \
    --PacketFilterConfig.PktlenMax 0 \
    --PacketFilterConfig.MatchLogic xx \
    --PacketFilterConfig.MatchBegin xx \
    --PacketFilterConfig.Offset 0 \
    --PacketFilterConfig.SportStart 0 \
    --PacketFilterConfig.DportStart 0 \
    --PacketFilterConfig.PktlenMin 0 \
    --PacketFilterConfig.IsNot2 0 \
    --PacketFilterConfig.Depth 0 \
    --PacketFilterConfig.Str xx \
    --PacketFilterConfig.Action xx \
    --PacketFilterConfig.Protocol xx \
    --PacketFilterConfig.MatchType xx \
    --PacketFilterConfig.DportEnd 0 \
    --PacketFilterConfig.Offset2 0 \
    --PacketFilterConfig.Depth2 0 \
    --PacketFilterConfig.Id xx
```

Output: 
```
{
    "Response": {
        "RequestId": "5063ab0a-a8a7-41e8-ace2-263b2c1c8794"
    }
}
```

