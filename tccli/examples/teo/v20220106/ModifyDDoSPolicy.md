**Example 1: 修改DDoS防护分区**



Input: 

```
tccli teo ModifyDDoSPolicy --cli-unfold-argument  \
    --DdosRule.DdosAntiPly.DestinationConnectLimit 0 \
    --DdosRule.DdosAntiPly.AbnormalSynNum 0 \
    --DdosRule.DdosAntiPly.ConnectTimeout 0 \
    --DdosRule.DdosAntiPly.DropOther xx \
    --DdosRule.DdosAntiPly.AbnormalConnectNum 0 \
    --DdosRule.DdosAntiPly.SourceCreateLimit 0 \
    --DdosRule.DdosAntiPly.DropTcp xx \
    --DdosRule.DdosAntiPly.DropUdp xx \
    --DdosRule.DdosAntiPly.EmptyConnectProtect xx \
    --DdosRule.DdosAntiPly.DropIcmp xx \
    --DdosRule.DdosAntiPly.SourceConnectLimit 0 \
    --DdosRule.DdosAntiPly.DestinationCreateLimit 1 \
    --DdosRule.DdosAntiPly.AbnormalSynRatio 0 \
    --DdosRule.DdosStatusInfo.AiStatus xx \
    --DdosRule.DdosStatusInfo.PlyLevel xx \
    --DdosRule.DdosStatusInfo.Appid xx \
    --DdosRule.Switch xx \
    --DdosRule.DdosAcl.Switch xx \
    --DdosRule.DdosAcl.Acl.0.Protocol xx \
    --DdosRule.DdosAcl.Acl.0.DportStart 0 \
    --DdosRule.DdosAcl.Acl.0.SportEnd 0 \
    --DdosRule.DdosAcl.Acl.0.Action xx \
    --DdosRule.DdosAcl.Acl.0.DportEnd 0 \
    --DdosRule.DdosAcl.Acl.0.SportStart 0 \
    --DdosRule.DdosGeoIp.Switch xx \
    --DdosRule.DdosGeoIp.RegionId 0 \
    --DdosRule.DdosPacketFilter.Switch xx \
    --DdosRule.DdosPacketFilter.PacketFilter.0.DportStart 0 \
    --DdosRule.DdosPacketFilter.PacketFilter.0.MatchType2 xx \
    --DdosRule.DdosPacketFilter.PacketFilter.0.MatchBegin2 xx \
    --DdosRule.DdosPacketFilter.PacketFilter.0.DportEnd 0 \
    --DdosRule.DdosPacketFilter.PacketFilter.0.MatchLogic xx \
    --DdosRule.DdosPacketFilter.PacketFilter.0.Offset2 0 \
    --DdosRule.DdosPacketFilter.PacketFilter.0.Str2 xx \
    --DdosRule.DdosPacketFilter.PacketFilter.0.PacketMax 0 \
    --DdosRule.DdosPacketFilter.PacketFilter.0.IsNot2 0 \
    --DdosRule.DdosPacketFilter.PacketFilter.0.Depth2 0 \
    --DdosRule.DdosPacketFilter.PacketFilter.0.Depth 0 \
    --DdosRule.DdosPacketFilter.PacketFilter.0.MatchBegin xx \
    --DdosRule.DdosPacketFilter.PacketFilter.0.SportEnd 0 \
    --DdosRule.DdosPacketFilter.PacketFilter.0.Str xx \
    --DdosRule.DdosPacketFilter.PacketFilter.0.Offset 0 \
    --DdosRule.DdosPacketFilter.PacketFilter.0.Action xx \
    --DdosRule.DdosPacketFilter.PacketFilter.0.Protocol xx \
    --DdosRule.DdosPacketFilter.PacketFilter.0.IsNot 0 \
    --DdosRule.DdosPacketFilter.PacketFilter.0.SportStart 0 \
    --DdosRule.DdosPacketFilter.PacketFilter.0.MatchType xx \
    --DdosRule.DdosPacketFilter.PacketFilter.0.PacketMin 0 \
    --DdosRule.DdosAllowBlock.Switch xx \
    --DdosRule.DdosAllowBlock.UserAllowBlockIp.0.Ip xx \
    --DdosRule.DdosAllowBlock.UserAllowBlockIp.0.UpdateTime 0 \
    --DdosRule.DdosAllowBlock.UserAllowBlockIp.0.Type xx \
    --DdosRule.DdosAllowBlock.UserAllowBlockIp.0.Mask 0 \
    --PolicyId 542 \
    --ZoneId xx
```

Output: 
```
{
    "Response": {
        "RequestId": "cb1f63d0-9173-4a1e-adb9-bd1ee2642b58",
        "PolicyId": 542
    }
}
```

