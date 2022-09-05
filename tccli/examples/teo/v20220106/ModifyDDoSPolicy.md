**Example 1: 修改DDoS防护分区-连接防护**

源站新建连接限速10000个/秒

Input: 

```
tccli teo ModifyDDoSPolicy --cli-unfold-argument  \
    --PolicyId 1 \
    --ZoneId zone-27filz8zp3vi \
    --DdosRule.DdosAntiPly.AbnormalConnectNum 0 \
    --DdosRule.DdosAntiPly.AbnormalSynNum 0 \
    --DdosRule.DdosAntiPly.AbnormalSynRatio 0 \
    --DdosRule.DdosAntiPly.ConnectTimeout 0 \
    --DdosRule.DdosAntiPly.DestinationConnectLimit 0 \
    --DdosRule.DdosAntiPly.DestinationCreateLimit 0 \
    --DdosRule.DdosAntiPly.DropIcmp on \
    --DdosRule.DdosAntiPly.DropOther off \
    --DdosRule.DdosAntiPly.DropTcp off \
    --DdosRule.DdosAntiPly.DropUdp off \
    --DdosRule.DdosAntiPly.EmptyConnectProtect 0 \
    --DdosRule.DdosAntiPly.SourceConnectLimit 0 \
    --DdosRule.DdosAntiPly.SourceCreateLimit 10000 \
    --DdosRule.DdosAntiPly.UdpShard off
```

Output: 
```
{
    "Response": {
        "RequestId": "cb1f63d0-9173-4a1e-adb9-bd1ee2642b58",
        "PolicyId": 1
    }
}
```

**Example 2: 修改DDoS防护分区-IP黑白名单**

1.1.1.1 拉黑

Input: 

```
tccli teo ModifyDDoSPolicy --cli-unfold-argument  \
    --PolicyId 1 \
    --ZoneId zone-27filz8zp3vi \
    --DdosRule.DdosAllowBlock.UserAllowBlockIp.0.Ip 1.1.1.1 \
    --DdosRule.DdosAllowBlock.UserAllowBlockIp.0.Mask 0 \
    --DdosRule.DdosAllowBlock.UserAllowBlockIp.0.Ip2  \
    --DdosRule.DdosAllowBlock.UserAllowBlockIp.0.Mask2 0 \
    --DdosRule.DdosAllowBlock.UserAllowBlockIp.0.Type block \
    --DdosRule.DdosAllowBlock.UserAllowBlockIp.0.UpdateTime 0
```

Output: 
```
{
    "Response": {
        "RequestId": "cb1f63d0-9173-4a1e-adb9-bd1ee2642b58",
        "PolicyId": 1
    }
}
```

