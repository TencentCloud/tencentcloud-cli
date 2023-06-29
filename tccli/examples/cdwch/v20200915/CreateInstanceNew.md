**Example 1: test**

创建集群API

Input: 

```
tccli cdwch CreateInstanceNew --cli-unfold-argument  \
    --InstanceName xzq-test-按量-hazk2节点 \
    --MountDiskType 0 \
    --HAZk True \
    --Zone ap-beijing-2 \
    --DataSpec.SpecName SCH1 \
    --DataSpec.Count 2 \
    --DataSpec.DiskSize 200 \
    --CommonSpec.SpecName SCH1 \
    --CommonSpec.Count 3 \
    --CommonSpec.DiskSize 100 \
    --HaFlag False \
    --UserVPCId vpc-8visjoh9 \
    --UserSubnetId subnet-03ij1dki \
    --ProductVersion 21.8.12.29 \
    --ChargeProperties.ChargeType POSTPAID_BY_HOUR
```

Output: 
```
{
    "Response": {
        "InstanceId": "cdwch-aijqera",
        "FlowId": "1231",
        "RequestId": "lweinasd-28kamasd-xasdas",
        "ErrorMsg": ""
    }
}
```

