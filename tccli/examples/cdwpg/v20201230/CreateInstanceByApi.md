**Example 1: 创建集群**

创建集群

Input: 

```
tccli cdwpg CreateInstanceByApi --cli-unfold-argument  \
    --InstanceName cdwpg_test001 \
    --Zone na-ashburn-1 \
    --UserVPCId vpc-65mchhgn \
    --UserSubnetId subnet-3b7g4en2 \
    --AdminPassword cloud_12345 \
    --ChargeProperties.ChargeType POSTPAID_BY_HOUR \
    --ChargeProperties.RenewFlag 0 \
    --ChargeProperties.TimeSpan 1 \
    --ChargeProperties.TimeUnit h \
    --Resources.0.Count 2 \
    --Resources.0.DiskSpec.DiskCount 1 \
    --Resources.0.DiskSpec.DiskSize 200 \
    --Resources.0.DiskSpec.DiskType CLOUD_HSSD \
    --Resources.0.SpecName S_4_16_H_CN \
    --Resources.0.Type cn \
    --Resources.1.Type dn \
    --Resources.1.SpecName S_4_16_H \
    --Resources.1.Count 2 \
    --Resources.1.DiskSpec.DiskType CLOUD_HSSD \
    --Resources.1.DiskSpec.DiskSize 20 \
    --Resources.1.DiskSpec.DiskCount 10
```

Output: 
```
{
    "Response": {
        "FlowId": "1125",
        "InstanceId": "cdwpg-fdergdabc",
        "ErrorMsg": "",
        "RequestId": "abc-sssscdddd"
    }
}
```

