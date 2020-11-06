**Example 1: 七层转发规则绑定目标组**



Input: 

```
tccli clb AssociateTargetGroups --cli-unfold-argument  \
    --Associations.0.LoadBalancerId lb-phbx2420 \
    --Associations.0.ListenerId lbl-m2q6sp9m \
    --Associations.0.LocationId loc-jjqr0ric \
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

