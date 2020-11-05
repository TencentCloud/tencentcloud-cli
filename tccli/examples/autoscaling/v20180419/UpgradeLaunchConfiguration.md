**Example 1: Upgrading a launch configuration with simple parameters**

This example shows you how to upgrade a launch configuration by only assigning values for the required parameters (launch configuration name, instance model, and image ID) and using system default values for other parameters. The specific configuration is as follows: launch configuration name: as_test, instance model: Standard II 1C1G (S2.SMALL1), image ID: img-8toqc6s3.

Input: 

```
tccli as UpgradeLaunchConfiguration --cli-unfold-argument  \
    --LaunchConfigurationId asc-gj14vczi\
    --LaunchConfigurationName as_test\
    --InstanceTypes S2.SMALL1\
    --ImageId img-8toqc6s3
```

Output: 
```
{
    "Response": {
        "RequestId": "d68a3364-a933-4664-bee4-fb89b8c69b49"
    }
}
```

**Example 2: Upgrading a launch configuration with detailed parameters**

This example shows you how to upgrade a launch configuration with the following configurations. Launch configuration name: as_test; image ID: img-8toqc6s3; model: Standard II 1C1G (S2.SMALL1); system disk: 50 GB local disk; data disk: 100 GB HDD cloud disk; public billing method: pay-as-you-go by traffic on an hourly basis; public network bandwidth cap: 5 Mbps; public IP: assigned; login method: key; Cloud Monitor service: enabled, Anti-DDoS: enabled

Input: 

```
tccli as UpgradeLaunchConfiguration --cli-unfold-argument  \
    --LaunchConfigurationId asc-gj14vczi\
    --LaunchConfigurationName as_test\
    --ImageId img-8toqc6s3\
    --InstanceTypes S2.SMALL1\
    --SystemDisk.DiskType LOCAL_BASIC\
    --SystemDisk.DiskSize 50\
    --DataDisks.0.DiskType CLOUD_BASIC\
    --DataDisks.0.DiskSize 100\
    --InternetAccessible.InternetChargeType TRAFFIC_POSTPAID_BY_HOUR\
    --InternetAccessible.InternetMaxBandwidthOut 5\
    --InternetAccessible.PublicIpAssigned TRUE\
    --LoginSettings.KeyIds skey-k8eypc1l\
    --EnhancedService.SecurityService.Enabled TRUE\
    --EnhancedService.MonitorService.Enabled TRUE
```

Output: 
```
{
    "Response": {
        "RequestId": "1430a2d3-eb73-44c6-8316-218c4562a85c"
    }
}
```

