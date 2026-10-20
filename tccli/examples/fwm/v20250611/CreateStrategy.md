**Example 1: 创建下发策略**



Input: 

```
tccli fwm CreateStrategy --cli-unfold-argument  \
    --Product cfw_edge_acl \
    --ReceiveAccount 100014712605 \
    --PreStrategy.0.GroupId fwmrg-a47wwiregj \
    --PreStrategy.0.Sequence 1 \
    --PostStrategy.0.GroupId fwmrg-a47wwiregj \
    --PostStrategy.0.Sequence 1
```

Output: 
```
{
    "Response": {
        "StrategyIds": [
            "fwms-r7glwuuy"
        ],
        "RequestId": "c7a2ed81-b669-4e09-a281-b20ba7899f69"
    }
}
```

