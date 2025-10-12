**Example 1: 创建执行资源组**



Input: 

```
tccli wedata CreateResourceGroup --cli-unfold-argument  \
    --Name test8 \
    --Type.ResourceGroupType Integration \
    --Type.Integration.OfflineDataSync.Specification integrated \
    --Type.Integration.OfflineDataSync.Number 2 \
    --AutoRenewEnabled False \
    --PurchasePeriod 1 \
    --VpcId vpc-4t9mtwbv \
    --SubNet subnet-h2ga4dks \
    --ResourceRegion ap-guangzhou \
    --AssociatedProjectId None \
    --Description None
```

Output: 
```
{
    "Response": {
        "Data": {
            "ResourceGroupId": "1757153576853",
            "Status": true
        },
        "RequestId": "a6e763a4-88d9-482d-b5fc-b7ff597446b9"
    }
}
```

