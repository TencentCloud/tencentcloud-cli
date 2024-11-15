**Example 1: Serverless HBase创建实例**

Serverless HBase创建实例

Input: 

```
tccli emr CreateSLInstance --cli-unfold-argument  \
    --InstanceName sl-haoyuhua-test-create \
    --PayMode 0 \
    --DiskType CLOUD_PREMIUM \
    --DiskSize 100 \
    --NodeType 4C16G \
    --ZoneSettings.0.Zone ap-guangzhou-2 \
    --ZoneSettings.0.VPCSettings.VpcId vpc-dcfhrh73 \
    --ZoneSettings.0.VPCSettings.SubnetId subnet-5bhc4kly \
    --ZoneSettings.0.NodeNum 1 \
    --ZoneSettings.1.Zone ap-guangzhou-2 \
    --ZoneSettings.1.VPCSettings.VpcId vpc-dcfhrh73 \
    --ZoneSettings.1.VPCSettings.SubnetId subnet-5bhc4kly \
    --ZoneSettings.1.NodeNum 1 \
    --ZoneSettings.2.Zone ap-guangzhou-2 \
    --ZoneSettings.2.VPCSettings.VpcId vpc-dcfhrh73 \
    --ZoneSettings.2.VPCSettings.SubnetId subnet-5bhc4kly \
    --ZoneSettings.2.NodeNum 1
```

Output: 
```
{
    "Response": {
        "InstanceId": "emr-8qrmc34c",
        "RequestId": "983e4dae-1cb4-40cb-8476-3231a6849696"
    }
}
```

