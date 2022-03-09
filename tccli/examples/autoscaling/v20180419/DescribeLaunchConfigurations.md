**Example 1: 根据启动配置ID查询启动配置列表**



Input: 

```
tccli as DescribeLaunchConfigurations --cli-unfold-argument  \
    --LaunchConfigurationIds asc-fa28v4in asc-g9uwgyvx
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
                        "SnapshotId": null,
                        "DeleteWithInstance": false
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
                    "MonitorService": {
                        "Enabled": true
                    }
                },
                "UserData": null,
                "InstanceTags": [],
                "CreatedTime": "2022-03-03T02:36:12Z",
                "UpdatedTime": "2022-03-03T06:49:31Z",
                "CamRoleName": "",
                "HostNameSettings": {
                    "HostName": null,
                    "HostNameStyle": null
                },
                "InstanceNameSettings": {
                    "InstanceName": "",
                    "InstanceNameStyle": ""
                },
                "InstanceChargePrepaid": {
                    "Period": 0,
                    "RenewFlag": ""
                }
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
                        "DeleteWithInstance": null
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
                    "MonitorService": {
                        "Enabled": true
                    }
                },
                "UserData": null,
                "InstanceTags": [],
                "CreatedTime": "2022-03-02T02:25:12Z",
                "UpdatedTime": "2022-03-02T02:25:12Z",
                "CamRoleName": "",
                "HostNameSettings": {
                    "HostName": null,
                    "HostNameStyle": null
                },
                "InstanceNameSettings": {
                    "InstanceName": "",
                    "InstanceNameStyle": ""
                },
                "InstanceChargePrepaid": {
                    "Period": 0,
                    "RenewFlag": ""
                }
            }
        ],
        "RequestId": "0d4514d4-e277-4f0f-bc85-8b7377a71980"
    }
}
```

**Example 2: 使用Filters查看启动配置列表**



Input: 

```
tccli as DescribeLaunchConfigurations --cli-unfold-argument  \
    --Filters.0.Name launch-configuration-id \
    --Filters.0.Values asc-fa28v4in
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
                        "DeleteWithInstance": false
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
                    "MonitorService": {
                        "Enabled": true
                    }
                },
                "UserData": null,
                "InstanceTags": [],
                "CreatedTime": "2022-03-03T02:36:12Z",
                "UpdatedTime": "2022-03-03T06:49:31Z",
                "CamRoleName": "",
                "HostNameSettings": {
                    "HostName": null,
                    "HostNameStyle": null
                },
                "InstanceNameSettings": {
                    "InstanceName": "",
                    "InstanceNameStyle": ""
                },
                "InstanceChargePrepaid": {
                    "Period": 0,
                    "RenewFlag": ""
                }
            }
        ],
        "RequestId": "923dd24c-e492-4bdb-90be-1d3bd4bfe8a5"
    }
}
```

