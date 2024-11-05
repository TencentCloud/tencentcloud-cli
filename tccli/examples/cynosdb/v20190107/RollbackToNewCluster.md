**Example 1: 回档到新集群**



Input: 

```
tccli cynosdb RollbackToNewCluster --cli-unfold-argument  \
    --Zone ap-guangzhou-5 \
    --UniqVpcId vpc-tsnp6wjk \
    --UniqSubnetId subnet-tsrq2i9e \
    --ClusterName MyClusterName \
    --RollbackId 1 \
    --OriginalClusterId cynosdbmysql-tsr2ubsj \
    --ExpectTime 2024-10-01 12:01:01 \
    --AutoVoucher 0 \
    --ResourceTags.0.TagKey tagKey-1 \
    --ResourceTags.0.TagValue tagValue-1 \
    --DbMode MYSQL \
    --MinCpu 0 \
    --MaxCpu 0 \
    --AutoPause yes \
    --AutoPauseDelay 0 \
    --SecurityGroupIds sg-sjcgywls \
    --AlarmPolicyIds policy-jylgsf32 \
    --ClusterParams.0.ParamName binlog_cache_size \
    --ClusterParams.0.CurrentValue 200 \
    --ClusterParams.0.OldValue 3000 \
    --ParamTemplateId 0 \
    --InstanceInitInfos.0.Cpu 1 \
    --InstanceInitInfos.0.Memory 2 \
    --InstanceInitInfos.0.InstanceType rw \
    --InstanceInitInfos.0.InstanceCount 1 \
    --InstanceInitInfos.0.MinRoCount 1 \
    --InstanceInitInfos.0.MaxRoCount 2 \
    --InstanceInitInfos.0.MinRoCpu 1 \
    --InstanceInitInfos.0.MaxRoCpu 4 \
    --DealMode 0
```

Output: 
```
{
    "Response": {
        "TranId": "12635123871523612735",
        "DealNames": [
            "126351238715236127011"
        ],
        "ResourceIds": [
            "cynosdbmysql-ins-tsk5bs6w"
        ],
        "ClusterIds": [
            "cynosdbmysql-kshc2bxu"
        ],
        "BigDealIds": [
            "12635123871523612735012"
        ],
        "RequestId": "91331f25-7342-4c58-925c-3deb5aee4a61"
    }
}
```

