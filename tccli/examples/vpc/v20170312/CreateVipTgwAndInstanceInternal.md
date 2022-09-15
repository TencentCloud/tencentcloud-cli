**Example 1: 添加VIP的TGW以及实例**



Input: 

```
tccli vpc CreateVipTgwAndInstanceInternal --cli-unfold-argument  \
    --AddVipTgwAndInstanceSet.0.Instance.0.TsvIp 1.1.1.1 \
    --AddVipTgwAndInstanceSet.0.Instance.0.ZoneId 100001 \
    --AddVipTgwAndInstanceSet.0.Vip 10.6.2.3 \
    --AddVipTgwAndInstanceSet.0.VpcId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

