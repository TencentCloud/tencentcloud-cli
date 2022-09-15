**Example 1: 更新VIP的TGW**



Input: 

```
tccli vpc UpdateVipTgwAndInstanceInternal --cli-unfold-argument  \
    --UpdateVipTgwAndInstanceSet.0.Instance.0.TsvIp 1.1.1.1 \
    --UpdateVipTgwAndInstanceSet.0.Instance.0.ZoneId 100001 \
    --UpdateVipTgwAndInstanceSet.0.Vip 10.6.2.3 \
    --UpdateVipTgwAndInstanceSet.0.VpcId 1 \
    --UpdateVipTgwAndInstanceSet.0.TsvIp 1.1.1.1
```

Output: 
```
{
    "Response": {
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

