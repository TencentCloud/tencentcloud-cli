**Example 1: 查询流量镜像过滤规则**



Input: 

```
tccli vpc DescribeTrafficMirrorFilterRules --cli-unfold-argument  \
    --TrafficMirrorId imgf-9ryixdn6 \
    --TrafficMirrorFilterRuleIds tmfi-bbc6a8cv
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
        "TotalCount": 2,
        "TrafficMirrorId": "imgf-9ryixdn6",
        "RequestId": "8984d5f4-72c1-4eae-9cc9-7dc2c346316d"
    }
}
```

