**Example 1: 创建工作空间**

创建工作空间

Input: 

```
tccli thpc CreateWorkspaces --cli-unfold-argument  \
    --SpaceChargeType PREPAID \
    --SpaceChargePrepaid.Period 1 \
    --SpaceChargePrepaid.RenewFlag NOTIFY_AND_AUTO_RENEW \
    --Placement.Zone ap-guangzhou-2 \
    --Placement.ProjectId 0 \
    --VirtualPrivateCloud.AsVpcGateway False \
    --VirtualPrivateCloud.VpcId vpc-nrqwfyzv \
    --VirtualPrivateCloud.SubnetId subnet-0tmm4ywk \
    --VirtualPrivateCloud.Ipv6AddressCount 0 \
    --SpaceType 96A.96XLARGE2304 \
    --ImageId img-9qrfy1xt \
    --SystemDisk.DiskSize 50 \
    --SystemDisk.DiskType CLOUD_PREMIUM \
    --DataDisks.0.DiskSize 50 \
    --DataDisks.0.DiskType CLOUD_PREMIUM \
    --DataDisks.1.DiskSize 50 \
    --DataDisks.1.DiskType CLOUD_PREMIUM \
    --InternetAccessible.PublicIpAssigned True \
    --InternetAccessible.InternetMaxBandwidthOut 5 \
    --SecurityGroupIds sg-fsx9rsr1 \
    --SpaceCount 1 \
    --EnhancedService.SecurityService.Enabled True \
    --EnhancedService.MonitorService.Enabled True \
    --EnhancedService.AutomationService.Enabled True
```

Output: 
```
{
    "Response": {
        "SpaceIdSet": [
            "wks-avs9gqvt"
        ],
        "RequestId": "efbbe00e-0175-4ee7-92c5-debc5763142d"
    }
}
```

