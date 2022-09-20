**Example 1: 修改DDoS防护分区-IP黑白名单**

1.1.1.1 拉黑

Input: 

```
tccli teo ModifyDDoSPolicy --cli-unfold-argument  \
    --PolicyId 1 \
    --ZoneId zone-27filz8zp3vi \
    --DDoSRule.DDoSAllowBlock.DDoSAllowBlockRules.0.Ip 1.1.1.1 \
    --DDoSRule.DDoSAllowBlock.DDoSAllowBlockRules.0.Type block \
    --DDoSRule.DDoSAllowBlock.DDoSAllowBlockRules.0.UpdateTime 0
```

Output: 
```
{
    "Response": {
        "RequestId": "cb1f63d0-9173-4a1e-adb9-bd1ee2642b58"
    }
}
```

**Example 2: 修改DDoS防护分区-连接防护**

源站新建连接限速10000个/秒

Input: 

```
tccli teo ModifyDDoSPolicy --cli-unfold-argument  \
    --PolicyId 1 \
    --ZoneId zone-27filz8zp3vi \
    --DDoSRule.DDoSAntiPly.AbnormalConnectNum 0 \
    --DDoSRule.DDoSAntiPly.AbnormalSynNum 0 \
    --DDoSRule.DDoSAntiPly.AbnormalSynRatio 0 \
    --DDoSRule.DDoSAntiPly.ConnectTimeout 0 \
    --DDoSRule.DDoSAntiPly.DestinationConnectLimit 0 \
    --DDoSRule.DDoSAntiPly.DestinationCreateLimit 0 \
    --DDoSRule.DDoSAntiPly.DropIcmp on \
    --DDoSRule.DDoSAntiPly.DropOther off \
    --DDoSRule.DDoSAntiPly.DropTcp off \
    --DDoSRule.DDoSAntiPly.DropUdp off \
    --DDoSRule.DDoSAntiPly.EmptyConnectProtect 0 \
    --DDoSRule.DDoSAntiPly.SourceConnectLimit 0 \
    --DDoSRule.DDoSAntiPly.SourceCreateLimit 10000 \
    --DDoSRule.DDoSAntiPly.UdpShard off
```

Output: 
```
{
    "Response": {
        "RequestId": "cb1f63d0-9173-4a1e-adb9-bd1ee2642b58"
    }
}
```

