**Example 1: 使用Filters查看启动配置列表**



Input: 

```
tccli as DescribeLaunchConfigurations --cli-unfold-argument  \
    --Filters.0.Values asc-fa28v4in \
    --Filters.0.Name launch-configuration-id
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "LaunchConfigurationSet": [
            {
                "ProjectId": 0,
                "LaunchConfigurationId": "asc-fa28v4in",
                "VersionNumber": 2,
                "LaunchConfigurationName": "lc1",
                "LaunchConfigurationStatus": "NORMAL",
                "AutoScalingGroupAbstractSet": [],
                "InstanceType": "S3.MEDIUM4",
                "InstanceTypes": [
                    "S3.MEDIUM4"
                ],
                "LastOperationInstanceTypesCheckPolicy": "ANY",
                "ImageId": "img-eb30mz89",
                "ImageFamily": "ubuntu-f0",
                "Tags": [],
                "IPv6InternetAccessible": {
                    "InternetChargeType": "TRAFFIC_POSTPAID_BY_HOUR",
                    "InternetMaxBandwidthOut": 0,
                    "BandwidthPackageId": null
                },
                "DisasterRecoverGroupIds": [],
                "InstanceChargeType": "POSTPAID_BY_HOUR",
                "InstanceMarketOptions": null,
                "DiskTypePolicy": "ORIGINAL",
                "SystemDisk": {
                    "DiskType": "CLOUD_PREMIUM",
                    "DiskSize": 50
                },
                "DataDisks": [
                    {
                        "DiskType": "CLOUD_PREMIUM",
                        "DiskSize": 10,
                        "SnapshotId": null,
                        "DeleteWithInstance": false,
                        "Encrypt": false,
                        "BurstPerformance": null,
                        "ThroughputPerformance": null
                    }
                ],
                "LoginSettings": {
                    "KeyIds": []
                },
                "InternetAccessible": {
                    "InternetChargeType": "TRAFFIC_POSTPAID_BY_HOUR",
                    "InternetMaxBandwidthOut": 0,
                    "PublicIpAssigned": false,
                    "BandwidthPackageId": null
                },
                "SecurityGroupIds": [],
                "EnhancedService": {
                    "SecurityService": {
                        "Enabled": true
                    },
                    "AutomationToolsService": {
                        "Enabled": true
                    },
                    "MonitorService": {
                        "Enabled": true
                    }
                },
                "UserData": null,
                "InstanceTags": [],
                "CreatedTime": "2022-03-03T02:36:12Z",
                "UpdatedTime": "2022-03-03T06:49:31Z",
                "CamRoleName": "CVM_QcsRole",
                "HostNameSettings": {
                    "HostName": null,
                    "HostNameSuffix": null,
                    "HostNameStyle": null
                },
                "InstanceNameSettings": {
                    "InstanceName": "ins-ubuntu-0",
                    "InstanceNameSuffix": null,
                    "InstanceNameStyle": "UNIQUE"
                },
                "InstanceChargePrepaid": {
                    "Period": 0,
                    "RenewFlag": "NOTIFY_AND_AUTO_RENEW"
                },
                "HpcClusterId": "hpc-u7y5r4e3"
            }
        ],
        "RequestId": "923dd24c-e492-4bdb-90be-1d3bd4bfe8a5"
    }
}
```

**Example 2: 根据启动配置ID查询启动配置列表**



Input: 

```
tccli as DescribeLaunchConfigurations --cli-unfold-argument  \
    --LaunchConfigurationIds asc-g9uwgyvx asc-fa28v4in
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "LaunchConfigurationSet": [
            {
                "ProjectId": 0,
                "LaunchConfigurationId": "asc-fa28v4in",
                "VersionNumber": 2,
                "LaunchConfigurationName": "lc1",
                "LaunchConfigurationStatus": "NORMAL",
                "AutoScalingGroupAbstractSet": [],
                "InstanceType": "S3.MEDIUM4",
                "InstanceTypes": [
                    "S3.MEDIUM4"
                ],
                "LastOperationInstanceTypesCheckPolicy": "ANY",
                "ImageId": "img-eb30mz89",
                "InstanceChargeType": "POSTPAID_BY_HOUR",
                "InstanceMarketOptions": null,
                "DiskTypePolicy": "ORIGINAL",
                "SystemDisk": {
                    "DiskType": "CLOUD_PREMIUM",
                    "DiskSize": 50
                },
                "DataDisks": [
                    {
                        "DiskType": "CLOUD_PREMIUM",
                        "DiskSize": 10,
                        "BurstPerformance": null,
                        "SnapshotId": null,
                        "DeleteWithInstance": false,
                        "Encrypt": false,
                        "ThroughputPerformance": null
                    }
                ],
                "LoginSettings": {
                    "KeyIds": []
                },
                "InternetAccessible": {
                    "InternetChargeType": "TRAFFIC_POSTPAID_BY_HOUR",
                    "InternetMaxBandwidthOut": 0,
                    "PublicIpAssigned": false,
                    "BandwidthPackageId": null
                },
                "SecurityGroupIds": [],
                "EnhancedService": {
                    "SecurityService": {
                        "Enabled": true
                    },
                    "AutomationToolsService": {
                        "Enabled": true
                    },
                    "MonitorService": {
                        "Enabled": true
                    }
                },
                "UserData": null,
                "InstanceTags": [],
                "ImageFamily": "ubuntu-f0",
                "Tags": [],
                "IPv6InternetAccessible": {
                    "InternetChargeType": "TRAFFIC_POSTPAID_BY_HOUR",
                    "InternetMaxBandwidthOut": 0,
                    "BandwidthPackageId": null
                },
                "DisasterRecoverGroupIds": [],
                "CreatedTime": "2022-03-03T02:36:12Z",
                "UpdatedTime": "2022-03-03T06:49:31Z",
                "CamRoleName": "CVM_QcsRole",
                "HostNameSettings": {
                    "HostName": null,
                    "HostNameSuffix": null,
                    "HostNameStyle": null
                },
                "InstanceNameSettings": {
                    "InstanceName": "ins-ubuntu-0",
                    "InstanceNameSuffix": null,
                    "InstanceNameStyle": "UNIQUE"
                },
                "InstanceChargePrepaid": {
                    "Period": 0,
                    "RenewFlag": "NOTIFY_AND_AUTO_RENEW"
                },
                "HpcClusterId": "hpc-u7y5r4e3"
            },
            {
                "ProjectId": 0,
                "LaunchConfigurationId": "asc-g9uwgyvx",
                "VersionNumber": 1,
                "LaunchConfigurationName": "lc2",
                "LaunchConfigurationStatus": "NORMAL",
                "AutoScalingGroupAbstractSet": [],
                "InstanceType": "S3.MEDIUM4",
                "InstanceTypes": [
                    "S3.MEDIUM4"
                ],
                "LastOperationInstanceTypesCheckPolicy": "ANY",
                "ImageId": "img-eb30mz89",
                "InstanceChargeType": "POSTPAID_BY_HOUR",
                "InstanceMarketOptions": null,
                "DiskTypePolicy": "ORIGINAL",
                "SystemDisk": {
                    "DiskType": "CLOUD_PREMIUM",
                    "DiskSize": 50
                },
                "DataDisks": [
                    {
                        "DiskType": "CLOUD_PREMIUM",
                        "DiskSize": 40,
                        "SnapshotId": null,
                        "DeleteWithInstance": null,
                        "Encrypt": null,
                        "BurstPerformance": null,
                        "ThroughputPerformance": null
                    }
                ],
                "LoginSettings": {
                    "KeyIds": []
                },
                "InternetAccessible": {
                    "InternetChargeType": "TRAFFIC_POSTPAID_BY_HOUR",
                    "InternetMaxBandwidthOut": 0,
                    "PublicIpAssigned": false,
                    "BandwidthPackageId": null
                },
                "SecurityGroupIds": [],
                "EnhancedService": {
                    "SecurityService": {
                        "Enabled": true
                    },
                    "AutomationToolsService": {
                        "Enabled": true
                    },
                    "MonitorService": {
                        "Enabled": true
                    }
                },
                "UserData": null,
                "InstanceTags": [],
                "ImageFamily": "ubuntu-f0",
                "Tags": [],
                "IPv6InternetAccessible": {
                    "InternetChargeType": "TRAFFIC_POSTPAID_BY_HOUR",
                    "InternetMaxBandwidthOut": 0,
                    "BandwidthPackageId": null
                },
                "DisasterRecoverGroupIds": [],
                "CreatedTime": "2022-03-02T02:25:12Z",
                "UpdatedTime": "2022-03-02T02:25:12Z",
                "CamRoleName": "CVM_QcsRole",
                "HostNameSettings": {
                    "HostName": null,
                    "HostNameSuffix": null,
                    "HostNameStyle": null
                },
                "InstanceNameSettings": {
                    "InstanceName": "ins-ubuntu-0",
                    "InstanceNameSuffix": null,
                    "InstanceNameStyle": "UNIQUE"
                },
                "InstanceChargePrepaid": {
                    "Period": 0,
                    "RenewFlag": "NOTIFY_AND_AUTO_RENEW"
                },
                "HpcClusterId": "hpc-u7y5r4e3"
            }
        ],
        "RequestId": "0d4514d4-e277-4f0f-bc85-8b7377a71980"
    }
}
```

**Example 3: 使用Filters通过Tag:Key方式查看启动配置列表。**



Input: 

```
tccli as DescribeLaunchConfigurations --cli-unfold-argument  \
    --Filters.0.Values v2 \
    --Filters.0.Name tag:k1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "LaunchConfigurationSet": [
            {
                "ProjectId": 0,
                "LaunchConfigurationId": "asc-0zri3ck1",
                "VersionNumber": 1,
                "LaunchConfigurationName": "test_tag_k1_v2",
                "LaunchConfigurationStatus": "NORMAL",
                "AutoScalingGroupAbstractSet": [],
                "InstanceType": "S5.MEDIUM4",
                "InstanceTypes": [
                    "S5.MEDIUM4"
                ],
                "LastOperationInstanceTypesCheckPolicy": "ANY",
                "ImageId": "img-eb30mz89",
                "InstanceChargeType": "POSTPAID_BY_HOUR",
                "InstanceMarketOptions": null,
                "DiskTypePolicy": "ORIGINAL",
                "SystemDisk": {
                    "DiskType": "CLOUD_PREMIUM",
                    "DiskSize": 50
                },
                "DataDisks": [
                    {
                        "DiskType": "CLOUD_PREMIUM",
                        "DiskSize": 40,
                        "BurstPerformance": null,
                        "SnapshotId": null,
                        "DeleteWithInstance": null,
                        "Encrypt": null,
                        "ThroughputPerformance": null
                    }
                ],
                "LoginSettings": {
                    "KeyIds": []
                },
                "InternetAccessible": {
                    "InternetChargeType": "TRAFFIC_POSTPAID_BY_HOUR",
                    "InternetMaxBandwidthOut": 0,
                    "PublicIpAssigned": false,
                    "BandwidthPackageId": null
                },
                "SecurityGroupIds": [],
                "EnhancedService": {
                    "SecurityService": {
                        "Enabled": true
                    },
                    "AutomationToolsService": {
                        "Enabled": true
                    },
                    "MonitorService": {
                        "Enabled": true
                    }
                },
                "UserData": null,
                "Tags": [],
                "InstanceTags": [],
                "ImageFamily": "ubuntu-f0",
                "IPv6InternetAccessible": {
                    "InternetChargeType": "TRAFFIC_POSTPAID_BY_HOUR",
                    "InternetMaxBandwidthOut": 0,
                    "BandwidthPackageId": null
                },
                "DisasterRecoverGroupIds": [],
                "CreatedTime": "2022-07-14T06:37:08Z",
                "UpdatedTime": "2022-07-14T06:37:08Z",
                "CamRoleName": "CVM_QcsRole",
                "HostNameSettings": {
                    "HostName": null,
                    "HostNameSuffix": null,
                    "HostNameStyle": null
                },
                "InstanceNameSettings": {
                    "InstanceName": "ins-ubuntu-0",
                    "InstanceNameSuffix": null,
                    "InstanceNameStyle": "UNIQUE"
                },
                "InstanceChargePrepaid": {
                    "Period": 0,
                    "RenewFlag": "NOTIFY_AND_AUTO_RENEW"
                },
                "HpcClusterId": "hpc-u7y5r4e3"
            }
        ],
        "RequestId": "8b8047bb-1372-4208-866e-a18e7b7547e9"
    }
}
```

