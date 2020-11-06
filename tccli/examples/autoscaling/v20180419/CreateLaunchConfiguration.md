**Example 1: Creating Using Only the Required Parameters**

Only assign values for the required parameters (launch configuration name, instance model, and image ID) and use system default values for other parameters. The specific configuration is as follows: launch configuration name: as_test, instance model: Standard II 1C1G (S2.SMALL1), image ID: img-8toqc6s3.

Input: 

```
tccli as CreateLaunchConfiguration --cli-unfold-argument  \
    --LaunchConfigurationName as_test \
    --InstanceType S2.SMALL1 \
    --ImageId img-8toqc6s3
```

Output: 
```
{
    "Response": {
        "LaunchConfigurationId": "asc-23h37kyn",
        "RequestId": "d639dd64-9e46-4246-b13c-80954f81c11b"
    }
}
```

**Example 2: Creating Using Detailed Parameters**

Launch configuration name: as_test; image ID: img-8toqc6s3; model: Standard II 1C1G (S2.SMALL1); system disk: 50 GB local disk; data disk: 100 GB HDD cloud disk; internet billing method: pay-as-you-go by traffic on an hourly basis; upper limit for internet bandwidth: 5 Mbps; IP: public IP; login method: key; Cloud Monitor and Cloud Security: installed.

Input: 

```
tccli as CreateLaunchConfiguration --cli-unfold-argument  \
    --LaunchConfigurationName as_test \
    --ImageId img-8toqc6s3 \
    --InstanceType S2.SMALL1 \
    --SystemDisk.DiskType LOCAL_BASIC \
    --SystemDisk.DiskSize 50 \
    --DataDisks.0.DiskType CLOUD_BASIC \
    --DataDisks.0.DiskSize 100 \
    --InternetAccessible.InternetChargeType TRAFFIC_POSTPAID_BY_HOUR \
    --InternetAccessible.InternetMaxBandwidthOut 5 \
    --InternetAccessible.PublicIpAssigned TRUE \
    --LoginSettings.KeyIds skey-k8eypc1l \
    --EnhancedService.SecurityService.Enabled TRUE \
    --EnhancedService.MonitorService.Enabled TRUE
```

Output: 
```
{
    "Response": {
        "LaunchConfigurationId": "asc-fdz8j7dh",
        "RequestId": "9a7209d3-2260-49d7-952a-dfa2001f8822"
    }
}
```

**Example 3: Creating a Spot Instance Configuration**

Launch configuration name: spot-test; model: Standard II 2C4G (S2.MEDIUM4); billing method: bidding (SPOTPAID); 

Input: 

```
tccli as CreateLaunchConfiguration --cli-unfold-argument  \
    --LaunchConfigurationName spot-test \
    --InstanceType S2.MEDIUM4 \
    --ImageId img-8toqc6s3 \
    --SystemDisk.DiskType CLOUD_PREMIUM \
    --SystemDisk.DiskSize 50 \
    --InternetAccessible.InternetChargeType TRAFFIC_POSTPAID_BY_HOUR \
    --InternetAccessible.InternetMaxBandwidthOut 20 \
    --InternetAccessible.PublicIpAssigned true \
    --InstanceChargeType SPOTPAID \
    --InstanceMarketOptions.MarketType spot \
    --InstanceMarketOptions.SpotOptions.MaxPrice 0.99 \
    --InstanceMarketOptions.SpotOptions.SpotInstanceType one-time
```

Output: 
```
{
    "Response": {
        "LaunchConfigurationId": "asc-hpzwe3o2",
        "RequestId": "ccfe3052-e9c9-47ee-bf3d-5bc2dfd972c0"
    }
}
```

**Example 4: Creating a Launch Configuration that Supports Multiple Instance Models**

This supports two instance models, namely, S2.SMALL2 and S2.SMALL4.

Input: 

```
tccli as CreateLaunchConfiguration --cli-unfold-argument  \
    --LaunchConfigurationName multi_instance_types \
    --InstanceTypes S2.SMALL2 S2.SMALL4 \
    --ImageId img-8toqc6s3
```

Output: 
```
{
    "Response": {
        "LaunchConfigurationId": "asc-77mh1cho",
        "RequestId": "2864c860-27a0-439e-a1e1-0003b76734e7"
    }
}
```

