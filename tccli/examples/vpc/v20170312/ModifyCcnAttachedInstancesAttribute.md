**Example 1: 修改云联网关联实例备注**



Input: 

```
tccli vpc ModifyCcnAttachedInstancesAttribute --cli-unfold-argument  \
    --CcnId ccn-gree226l \
    --Instances.0.InstanceType VPC \
    --Instances.0.InstanceId vpc-3dr1zrr9 \
    --Instances.0.InstanceRegion ap-guangzhou \
    --Instances.0.Description test0 \
    --Instances.1.InstanceType DIRECTCONNECT \
    --Instances.1.InstanceId dcg-98qosdc3 \
    --Instances.1.InstanceRegion ap-guangzhou \
    --Instances.1.Description test1
```

Output: 
```
{
    "Response": {
        "RequestId": "627c2362-890f-4f9e-9158-5e457b80d48b"
    }
}
```

