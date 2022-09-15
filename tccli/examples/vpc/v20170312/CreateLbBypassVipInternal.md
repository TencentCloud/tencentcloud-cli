**Example 1: 用于添加安全组自动放通的VIP**



Input: 

```
tccli vpc CreateLbBypassVipInternal --cli-unfold-argument  \
    --AddLbBypassVipSet.0.Owner 123456 \
    --AddLbBypassVipSet.0.Vip 10.19.165.3 \
    --AddLbBypassVipSet.0.VpcId 1 \
    --AddLbBypassVipSet.0.UniqueVpcId vpc-jmaywf6r
```

Output: 
```
{
    "Response": {
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

