**Example 1: 创建流量镜像过滤规则**

创建流量镜像过滤规则

Input: 

```
tccli vpc CreateTrafficMirrorFilterRules --cli-unfold-argument  \
    --TrafficMirrorId imgf-9ryixdn6 \
    --IngressFilterRules.0.SrcNet 192.168.0.0/16 \
    --IngressFilterRules.0.DstNet 10.0.0.0/16 \
    --IngressFilterRules.0.Protocol TCP \
    --IngressFilterRules.0.SrcPort 1000-2000 \
    --IngressFilterRules.0.DstPort 1000-2000 \
    --IngressFilterRules.0.Priority 1 \
    --IngressFilterRules.0.Action ACCEPT \
    --IngressFilterRules.0.Description rule_1 \
    --EgressFilterRules.0.SrcNet 192.168.0.0/16 \
    --EgressFilterRules.0.DstNet 10.0.0.0/16 \
    --EgressFilterRules.0.Protocol TCP \
    --EgressFilterRules.0.SrcPort 2000-3000 \
    --EgressFilterRules.0.DstPort 2000-3000 \
    --EgressFilterRules.0.Priority 1 \
    --EgressFilterRules.0.Action DROP \
    --EgressFilterRules.0.Description rule_1
```

Output: 
```
{
    "Response": {
        "EgressFilterRules": [
            {
                "Action": "DROP",
                "CreatedTime": "2026-03-30 20:50:13",
                "Description": "rule_1",
                "DstNet": "10.0.0.0/16",
                "DstPort": "2000-3000",
                "Priority": 1,
                "Protocol": "TCP",
                "SrcNet": "192.168.0.0/16",
                "SrcPort": "2000-3000",
                "TrafficMirrorFilterRuleId": "tmfi-bbc6a8cv"
            }
        ],
        "IngressFilterRules": [
            {
                "Action": "ACCEPT",
                "CreatedTime": "2026-03-30 20:50:13",
                "Description": "rule_1",
                "DstNet": "10.0.0.0/16",
                "DstPort": "1000-2000",
                "Priority": 1,
                "Protocol": "TCP",
                "SrcNet": "192.168.0.0/16",
                "SrcPort": "1000-2000",
                "TrafficMirrorFilterRuleId": "tmfi-7gk0gtdz"
            }
        ],
        "TrafficMirrorId": "imgf-9ryixdn6",
        "RequestId": "a5358fa4-7656-4fcc-a5bd-b338e74f3ff2"
    }
}
```

