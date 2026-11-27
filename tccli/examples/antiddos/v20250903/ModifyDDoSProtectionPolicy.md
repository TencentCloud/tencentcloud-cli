**Example 1: 按防护实例 ID 全量修改 DDoS 防护策略**

将防护实例 `prot-3xua1doxm4km` 的 DDoS 防护策略一次性修改为：防护等级 `medium`；丢弃来自 `1.14.55.227` 的流量；对 TCP 80 端口继续防护并限速 100000000 bps、100000 pps；丢弃载荷中包含 `EVIL_TEST_PAYLOAD` 的报文；封禁中国香港地域；开启 `ICMP` 与其他协议封禁；开启源/目的 IP 新建连接数、并发连接数及异常连接防护；关闭流量签名校验。

Input: 

```
tccli antiddos ModifyDDoSProtectionPolicy --cli-unfold-argument  \
    --ProtectionId prot-3xua1doxm4km \
    --ProtectionPolicy.DefaultProtection.SensitivityLevel medium \
    --ProtectionPolicy.IPACLRules.Rules.0.Action drop \
    --ProtectionPolicy.IPACLRules.Rules.0.IPs 1.14.55.227 \
    --ProtectionPolicy.PortACLRules.Rules.0.SourcePortRange.FromPort 1 \
    --ProtectionPolicy.PortACLRules.Rules.0.SourcePortRange.ToPort 65535 \
    --ProtectionPolicy.PortACLRules.Rules.0.DestinationPortRange.FromPort 80 \
    --ProtectionPolicy.PortACLRules.Rules.0.DestinationPortRange.ToPort 80 \
    --ProtectionPolicy.PortACLRules.Rules.0.Protocol tcp \
    --ProtectionPolicy.PortACLRules.Rules.0.Action forward \
    --ProtectionPolicy.SpeedLimitRules.Rules.0.IPProtocolNumbers 6 \
    --ProtectionPolicy.SpeedLimitRules.Rules.0.DestinationPortRanges.0.FromPort 80 \
    --ProtectionPolicy.SpeedLimitRules.Rules.0.DestinationPortRanges.0.ToPort 80 \
    --ProtectionPolicy.SpeedLimitRules.Rules.0.Mode destination_ip \
    --ProtectionPolicy.SpeedLimitRules.Rules.0.BandwidthLimit 100000000 \
    --ProtectionPolicy.SpeedLimitRules.Rules.0.PacketRateLimit 100000 \
    --ProtectionPolicy.PacketFilterRules.Rules.0.Action drop \
    --ProtectionPolicy.PacketFilterRules.Rules.0.Protocol tcp \
    --ProtectionPolicy.PacketFilterRules.Rules.0.PacketSizeRange.Min 0 \
    --ProtectionPolicy.PacketFilterRules.Rules.0.PacketSizeRange.Max 1500 \
    --ProtectionPolicy.PacketFilterRules.Rules.0.SourcePortRange.FromPort 1 \
    --ProtectionPolicy.PacketFilterRules.Rules.0.SourcePortRange.ToPort 65535 \
    --ProtectionPolicy.PacketFilterRules.Rules.0.DestinationPortRange.FromPort 80 \
    --ProtectionPolicy.PacketFilterRules.Rules.0.DestinationPortRange.ToPort 80 \
    --ProtectionPolicy.PacketFilterRules.Rules.0.PacketFilterConditions.0.MatchBegin payload \
    --ProtectionPolicy.PacketFilterRules.Rules.0.PacketFilterConditions.0.Content.Type string \
    --ProtectionPolicy.PacketFilterRules.Rules.0.PacketFilterConditions.0.Content.Value EVIL_TEST_PAYLOAD \
    --ProtectionPolicy.PacketFilterRules.Rules.0.PacketFilterConditions.0.Content.Offset 0 \
    --ProtectionPolicy.PacketFilterRules.Rules.0.PacketFilterConditions.0.Content.Depth 100 \
    --ProtectionPolicy.GeoBlocking.GeoCode CN-HK \
    --ProtectionPolicy.ProtocolBlocking.TCPProtocol off \
    --ProtectionPolicy.ProtocolBlocking.UDPProtocol off \
    --ProtectionPolicy.ProtocolBlocking.ICMPProtocol on \
    --ProtectionPolicy.ProtocolBlocking.OtherProtocol on \
    --ProtectionPolicy.ConnectionProtection.SourceIPNewConnectionLimit 1000 \
    --ProtectionPolicy.ConnectionProtection.SourceIPConcurrentConnectionLimit 2000 \
    --ProtectionPolicy.ConnectionProtection.DestinationIPNewConnectionLimit 5000 \
    --ProtectionPolicy.ConnectionProtection.DestinationIPConcurrentConnectionLimit 10000 \
    --ProtectionPolicy.ConnectionProtection.AbnormalConnectionLimit.AbnormalConnectThreshold 1000 \
    --ProtectionPolicy.ConnectionProtection.AbnormalConnectionLimit.AbnormalConnectCondition.SynRatioThreshold 80 \
    --ProtectionPolicy.ConnectionProtection.AbnormalConnectionLimit.AbnormalConnectCondition.SynCountThreshold 1000 \
    --ProtectionPolicy.ConnectionProtection.AbnormalConnectionLimit.AbnormalConnectCondition.ConnectTimeout 10 \
    --ProtectionPolicy.ConnectionProtection.AbnormalConnectionLimit.AbnormalConnectCondition.EmptyConnection on \
    --ProtectionPolicy.TrafficSignature.Switch off \
    --ProtectionPolicy.TrafficSignature.TrafficSignatureKeys 0123456789abcdef-1A2B-0123456789abcdef0123456789abcdef01234567 \
    --ProtectionPolicy.TrafficSignature.UdpCheckPortRanges.0.FromPort 53 \
    --ProtectionPolicy.TrafficSignature.UdpCheckPortRanges.0.ToPort 53 \
    --ProtectionPolicy.TrafficSignature.TcpCheckPortRanges.0.FromPort 80 \
    --ProtectionPolicy.TrafficSignature.TcpCheckPortRanges.0.ToPort 80 \
    --ProtectionPolicy.TrafficSignature.UdpTrafficSignatureOffset 0 \
    --ProtectionPolicy.TrafficSignature.TcpTrafficSignatureOffset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "ad0d5d7b-2f9b-4f68-a595-e4dfa8c3f787"
    }
}
```

