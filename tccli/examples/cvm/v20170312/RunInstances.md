**Example 1: Purchasing a CDH instance**

This example shows you how to purchase one instance with the following configurations. Availability zone: Shanghai Zone 2; CDH: host-q88gab4i; image ID: img-pmqg1cw7; billing method: billed together with the CDH; model: 1C1G; system disk: 50 GB Premium Cloud Storage; data disk: 100 GB Premium Cloud Storage; network type: VPC; public network billing: pay-as-you-go by traffic on an hourly basis; public network bandwidth cap: 10 Mbps; public IP: randomly assigned; instance name: QCLOUD-TEST; login password: Qcloud@TestApi123++; Cloud Monitoring service: enabled; Anti-DDoS: enabled.

Input: 

```
tccli cvm RunInstances --cli-unfold-argument  \
    --Placement.Zone ap-shanghai-2 \
    --Placement.HostIds host-q88gab4i \
    --InstanceChargeType CDHPAID \
    --ImageId img-pmqg1cw7 \
    --InstanceType CDH_1C1G \
    --SystemDisk.DiskType CLOUD_PREMIUM \
    --SystemDisk.DiskSize 50 \
    --DataDisks.0.DiskType CLOUD_PREMIUM \
    --DataDisks.0.DiskSize 100 \
    --InternetAccessible.InternetChargeType TRAFFIC_POSTPAID_BY_HOUR \
    --InternetAccessible.InternetMaxBandwidthOut 10 \
    --InternetAccessible.PublicIpAssigned TRUE \
    --InstanceName QCLOUD-TEST \
    --LoginSettings.Password Qcloud@TestApi123++ \
    --EnhancedService.SecurityService.Enabled TRUE \
    --EnhancedService.MonitorService.Enabled TRUE \
    --InstanceCount 1
```

Output: 
```
{
    "Response": {
        "InstanceIdSet": [
            "ins-0s7wsh5x"
        ],
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

**Example 2: Purchasing an instance with only the required parameters**

This example shows you how to create an instance using only the required `Placement.Zone` and `ImageId` parameters. The other parameters use system default values. The instance is created in Shanghai Zone 2 with the image `img-pmqg1cw7`.

Input: 

```
tccli cvm RunInstances --cli-unfold-argument  \
    --Placement.Zone ap-shanghai-2 \
    --ImageId img-pmqg1cw7
```

Output: 
```
{
    "Response": {
        "InstanceIdSet": [
            "ins-1vogaxgk"
        ],
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

**Example 3: Purchasing a pay-as-you-go instance billed on an hourly basis**

This example shows you how to purchase one 64C128G standard (S5.16XLARGE256) instance in Shanghai Zone 2 using the image `img-pmqg1cw7`. The other configurations are as follows: billing method: pay-as-you-go on an hourly basis; system disk: 50 GB Premium Cloud Storage; data disk: 100 GB Premium Cloud Storage; network type: VPC; public network billing: pay-as-you-go by traffic on an hourly basis; public network bandwidth cap: 10 Mbps; public IP: randomly assigned; instance name: QCLOUD-TEST; login password: Qcloud@TestApi123++; Cloud Monitoring service: enabled; Anti-DDoS: enabled.

Input: 

```
tccli cvm RunInstances --cli-unfold-argument  \
    --Placement.Zone ap-shanghai-2 \
    --InstanceChargeType POSTPAID_BY_HOUR \
    --ImageId img-pmqg1cw7 \
    --InstanceType S5.16XLARGE256 \
    --SystemDisk.DiskType CLOUD_PREMIUM \
    --SystemDisk.DiskSize 50 \
    --DataDisks.0.DiskType CLOUD_PREMIUM \
    --DataDisks.0.DiskSize 100 \
    --InternetAccessible.InternetChargeType TRAFFIC_POSTPAID_BY_HOUR \
    --InternetAccessible.InternetMaxBandwidthOut 10 \
    --InternetAccessible.PublicIpAssigned TRUE \
    --InstanceName QCLOUD-TEST \
    --LoginSettings.Password Qcloud@TestApi123++ \
    --EnhancedService.SecurityService.Enabled TRUE \
    --EnhancedService.MonitorService.Enabled TRUE \
    --InstanceCount 1
```

Output: 
```
{
    "Response": {
        "InstanceIdSet": [
            "ins-32kcaqoa"
        ],
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

**Example 4: Creating an instance with the VPC IP address specified**

This example shows you how to purchase two instances with the following configurations. Availability zone: Shanghai Zone 2; billing method: pay-as-you-go on an hourly basis; image ID: img-dkwyg6sr; model: 64C128G standard (S5.16XLARGE256); system disk: 50 GB Premium Cloud Storage; network: VPC; VPC ID: 1urkhbj4; subnet ID: dcs9x3gz; VPC IP address: 10.0.0.18, and 10.0.0.19.

Input: 

```
tccli cvm RunInstances --cli-unfold-argument  \
    --InstanceType S5.16XLARGE256 \
    --SystemDisk.DiskType CLOUD_PREMIUM \
    --SystemDisk.DiskSize 50 \
    --Placement.Zone ap-shanghai-2 \
    --ImageId img-dkwyg6sr \
    --VirtualPrivateCloud.SubnetId subnet-dcs9x3gz \
    --VirtualPrivateCloud.VpcId vpc-1urkhbj4 \
    --VirtualPrivateCloud.PrivateIpAddresses 10.0.0.18 10.0.0.19 \
    --InstanceCount 2
```

Output: 
```
{
    "Response": {
        "InstanceIdSet": [
            "ins-0s7wsh5x",
            "ins-03lw8hok"
        ],
        "RequestId": "3c14def19-cfes-470e-b241-90787u6jf5uj"
    }
}
```

**Example 5: Purchasing a monthly subscription instance**

This example shows you how to query the price for purchasing one 64C128G standard (S5.16XLARGE256) instance in Shanghai Zone 2 using the image `img-pmqg1cw7`. The other configurations are as follows: billing method: monthly subscription for one month with auto-renewal upon expiration; system disk: 50 GB Premium Cloud Storage; data disk: 100 GB Premium Cloud Storage; network type: VPC; public network billing: pay-as-you-go by traffic on an hourly basis; public network bandwidth cap: 10 Mbps; public IP: randomly assigned; instance name: QCLOUD-TEST; login password: Qcloud@TestApi123++; Cloud Monitoring service: enabled; Anti-DDoS: enabled.

Input: 

```
tccli cvm RunInstances --cli-unfold-argument  \
    --Placement.Zone ap-shanghai-2 \
    --InstanceChargeType PREPAID \
    --InstanceChargePrepaid.Period 1 \
    --InstanceChargePrepaid.RenewFlag NOTIFY_AND_AUTO_RENEW \
    --ImageId img-pmqg1cw7 \
    --InstanceType S5.16XLARGE256 \
    --SystemDisk.DiskType CLOUD_PREMIUM \
    --SystemDisk.DiskSize 50 \
    --DataDisks.0.DiskType CLOUD_PREMIUM \
    --DataDisks.0.DiskSize 100 \
    --InternetAccessible.InternetChargeType TRAFFIC_POSTPAID_BY_HOUR \
    --InternetAccessible.InternetMaxBandwidthOut 10 \
    --InternetAccessible.PublicIpAssigned TRUE \
    --InstanceName QCLOUD-TEST \
    --LoginSettings.Password Qcloud@TestApi123++ \
    --EnhancedService.SecurityService.Enabled TRUE \
    --EnhancedService.MonitorService.Enabled TRUE \
    --InstanceCount 1
```

Output: 
```
{
    "Response": {
        "InstanceIdSet": [
            "ins-bfw5zq3y"
        ],
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

