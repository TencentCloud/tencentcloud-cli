**Example 1: 解除负载均衡和目标组的关联关系**



Input: 

```
tccli gwlb DisassociateTargetGroups --cli-unfold-argument  \
    --Associations.0.LoadBalancerId gwlb-20dhh498 \
    --Associations.0.TargetGroupId lbtg-xxqr0ric
```

Output: 
```
{
    "Response": {
        "RequestId": "bc953deb-02d7-4bd3-86a6-80421ec37776"
    }
}
```

