**Example 1: 快照策略关联实例**



Input: 

```
tccli vpc AttachSnapshotInstances --cli-unfold-argument  \
    --SnapshotPolicyId sspolicy-g6jwvm35 \
    --Instances.0.InstanceId sg-e18r37v3 \
    --Instances.0.InstanceType securitygroup \
    --Instances.0.InstanceRegion ap-shanghai
```

Output: 
```
{
    "Response": {
        "RequestId": "a38579de-a046-4d68-b24a-b629c8d0ae57"
    }
}
```

