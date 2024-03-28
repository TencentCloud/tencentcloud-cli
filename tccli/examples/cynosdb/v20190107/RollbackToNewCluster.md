**Example 1: 回档到新集群**



Input: 

```
tccli cynosdb RollbackToNewCluster --cli-unfold-argument  \
    --Zone abc \
    --UniqVpcId abc \
    --UniqSubnetId abc \
    --ClusterName abc \
    --RollbackId 1 \
    --OriginalClusterId abc \
    --ExpectTime abc \
    --AutoVoucher 0 \
    --ResourceTags.0.TagKey abc \
    --ResourceTags.0.TagValue abc \
    --DbMode abc \
    --MinCpu 0 \
    --MaxCpu 0 \
    --AutoPause abc \
    --AutoPauseDelay 0 \
    --SecurityGroupIds abc \
    --AlarmPolicyIds abc \
    --ClusterParams.0.ParamName abc \
    --ClusterParams.0.CurrentValue abc \
    --ClusterParams.0.OldValue abc \
    --ParamTemplateId 0 \
    --InstanceInitInfos.0.Cpu 0 \
    --InstanceInitInfos.0.Memory 0 \
    --InstanceInitInfos.0.InstanceType abc \
    --InstanceInitInfos.0.InstanceCount 0 \
    --InstanceInitInfos.0.MinRoCount 0 \
    --InstanceInitInfos.0.MaxRoCount 0 \
    --InstanceInitInfos.0.MinRoCpu 0 \
    --InstanceInitInfos.0.MaxRoCpu 0 \
    --DealMode 0
```

Output: 
```
{
    "Response": {
        "TranId": "abc",
        "DealNames": [
            "abc"
        ],
        "ResourceIds": [
            "abc"
        ],
        "ClusterIds": [
            "abc"
        ],
        "BigDealIds": [
            "abc"
        ],
        "RequestId": "abc"
    }
}
```

