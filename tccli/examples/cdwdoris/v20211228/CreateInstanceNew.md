**Example 1: 集群创建示例**

创建集群

Input: 

```
tccli cdwdoris CreateInstanceNew --cli-unfold-argument  \
    --InstanceName test-按量-hazk2节点 \
    --Zone ap-beijing-2 \
    --FeSpec.SpecName S_4_16_H \
    --FeSpec.Count 3 \
    --FeSpec.DiskSize 200 \
    --BeSpec.SpecName S_4_16_H \
    --BeSpec.Count 3 \
    --BeSpec.DiskSize 1000 \
    --HaFlag True \
    --UserVPCId vpc-8visjoh9 \
    --UserSubnetId subnet-03ij1dki \
    --ProductVersion 1.2 \
    --DorisUserPwd ujA7xa2*1 \
    --ChargeProperties.ChargeType POSTPAID_BY_HOUR
```

Output: 
```
{
    "Response": {
        "InstanceId": "cdwdoris-aijqera",
        "FlowId": "1231",
        "RequestId": "lweinasd-28kamasd-xasdas",
        "ErrorMsg": ""
    }
}
```

