**Example 1: 负载均衡关联目标组**



Input: 

```
tccli gwlb AssociateTargetGroups --cli-unfold-argument  \
    --Associations.0.LoadBalancerId gwlb-20dhh498 \
    --Associations.0.TargetGroupId lbtg-5xunivs0
```

Output: 
```
{
    "Response": {
        "RequestId": "dd2f3116-421c-4eda-8401-b9ddefcc65d5"
    }
}
```

