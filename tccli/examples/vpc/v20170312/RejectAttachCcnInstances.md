**Example 1: 云联网拒绝关联实例**



Input: 

```
tccli vpc RejectAttachCcnInstances --cli-unfold-argument  \
    --CcnId ccn-gree226l \
    --Instances.0.InstanceType VPC \
    --Instances.0.InstanceId vpc-3dr1zrr9 \
    --Instances.0.InstanceRegion ap-guangzhou
```

Output: 
```
{
    "Response": {
        "RequestId": "627c2362-890f-4f9e-9158-5e457b80d48b"
    }
}
```

