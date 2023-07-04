**Example 1: 云联网关联多个网络实例**

云联网关联多个网络实例

Input: 

```
tccli vpc AttachCcnInstances --cli-unfold-argument  \
    --CcnId ccn-gree226l \
    --Instances.0.InstanceType VPC \
    --Instances.0.InstanceId vpc-3dr1zrr9 \
    --Instances.0.InstanceRegion ap-guangzhou \
    --Instances.1.InstanceType DIRECTCONNECT \
    --Instances.1.InstanceId dcg-98qosdc3 \
    --Instances.1.InstanceRegion ap-guangzhou
```

Output: 
```
{
    "Response": {
        "RequestId": "627c2362-890f-4f9e-9158-5e457b80d48b"
    }
}
```

