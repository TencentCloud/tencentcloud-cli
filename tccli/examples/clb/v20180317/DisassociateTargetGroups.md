**Example 1: 解绑规则与目标组的关联关系**



Input: 

```
tccli clb DisassociateTargetGroups --cli-unfold-argument  \
    --Associations.0.LoadBalancerId lb-phbx2420 \
    --Associations.0.ListenerId lbl-m2q6sp9m \
    --Associations.0.LocationId loc-jjqr0ric \
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

