**Example 1: Using Filters to view the list of launch configurations**



Input: 

```
tccli as DescribeLaunchConfigurations --cli-unfold-argument  \
    --Filters.0.Name launch-configuration-id \
    --Filters.0.Values asc-l7rduvv0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "LaunchConfigurationSet": [
            {
                "ProjectId": 0,
                "LaunchConfigurationId": "asc-l7rduvv0",
                "VersionNumber": 1,
                "LaunchConfigurationName": "lc2",
                "AutoScalingGroupAbstractSet": [],
                "InstanceType": "S2.SMALL2",
                "InstanceTypes": [
                    "S2.SMALL2"
                ],
                "InstanceChargeType": "POSTPAID_BY_HOUR",
                "InstanceMarketOptions": null,
                "SystemDisk": {
                    "DiskType": "LOCAL_BASIC",
                    "DiskSize": 50
                },
                "DataDisks": [
                    {
                        "DiskType": "LOCAL_BASIC",
                        "DiskSize": 50
                    }
                ],
                "LoginSettings": {
                    "KeyIds": []
                },
                "InternetAccessible": {
                    "InternetChargeType": "BANDWIDTH_POSTPAID_BY_HOUR",
                    "InternetMaxBandwidthOut": 1,
                    "PublicIpAssigned": true
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
                "CreatedTime": "2018-05-03T03:23:10Z",
                "UpdatedTime": "2018-05-03T03:23:10Z"
            }
        ],
        "RequestId": "15f9582f-72ff-4b5f-91b6-ff905782391b"
    }
}
```

**Example 2: Querying the list of launch configurations by launch configuration ID**



Input: 

```
tccli as DescribeLaunchConfigurations --cli-unfold-argument  \
    --LaunchConfigurationIds asc-l7rduvv0 asc-2ejax3t8
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "LaunchConfigurationSet": [
            {
                "ProjectId": 0,
                "LaunchConfigurationId": "asc-2ejax3t8",
                "VersionNumber": 1,
                "LaunchConfigurationName": "lc1",
                "AutoScalingGroupAbstractSet": [],
                "InstanceType": "D1.2XLARGE32",
                "InstanceTypes": [
                    "D1.2XLARGE32"
                ],
                "InstanceChargeType": "POSTPAID_BY_HOUR",
                "InstanceMarketOptions": null,
                "SystemDisk": {
                    "DiskType": "LOCAL_BASIC",
                    "DiskSize": 50
                },
                "DataDisks": [],
                "LoginSettings": {
                    "KeyIds": []
                },
                "InternetAccessible": {
                    "InternetChargeType": "TRAFFIC_POSTPAID_BY_HOUR",
                    "InternetMaxBandwidthOut": 0,
                    "PublicIpAssigned": false
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
                "CreatedTime": "2018-05-03T06:37:48Z",
                "UpdatedTime": "2018-05-03T06:37:48Z"
            },
            {
                "ProjectId": 0,
                "LaunchConfigurationId": "asc-l7rduvv0",
                "VersionNumber": 1,
                "LaunchConfigurationName": "lc2",
                "AutoScalingGroupAbstractSet": [],
                "InstanceType": "S2.SMALL2",
                "InstanceTypes": [
                    "S2.SMALL2"
                ],
                "InstanceChargeType": "POSTPAID_BY_HOUR",
                "InstanceMarketOptions": null,
                "SystemDisk": {
                    "DiskType": "LOCAL_BASIC",
                    "DiskSize": 50
                },
                "DataDisks": [
                    {
                        "DiskType": "LOCAL_BASIC",
                        "DiskSize": 50
                    }
                ],
                "LoginSettings": {
                    "KeyIds": []
                },
                "InternetAccessible": {
                    "InternetChargeType": "BANDWIDTH_POSTPAID_BY_HOUR",
                    "InternetMaxBandwidthOut": 1,
                    "PublicIpAssigned": true
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
                "CreatedTime": "2018-05-03T03:23:10Z",
                "UpdatedTime": "2018-05-03T03:23:10Z"
            }
        ],
        "RequestId": "f7dd68bc-d5e3-4a43-92a5-bde6d8fe9bd4"
    }
}
```

