**Example 1: 查看实例列表**

查看在广州一区或广州二区的实例信息，限制返回结果最多为一项

Input: 

```
tccli cvm DescribeInstances --cli-unfold-argument  \
    --Limit 1 \
    --Filters.0.Values ap-guangzhou-2 ap-guangzhou-1 \
    --Filters.0.Name zone \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "InstanceSet": [
            {
                "RenewFlag": "NOTIFY_AND_MANUAL_RENEW",
                "Uuid": "e85f1388-0422-410d-8e50-bef540e78c18",
                "InstanceState": "RUNNING",
                "LatestOperationState": "SUCCESS",
                "LoginSettings": {
                    "Password": "123qwe!@#QWE",
                    "KeepImageLogin": "False",
                    "KeyIds": [
                        "skey-b4vakk62"
                    ]
                },
                "IPv6Addresses": [
                    "2001:0db8:86a3:08d3:1319:8a2e:0370:7344"
                ],
                "DedicatedClusterId": "",
                "RestrictState": "PROTECTIVELY_ISOLATED",
                "ExpiredTime": "2020-09-22T00:00:00+00:00",
                "DisasterRecoverGroupId": "",
                "Memory": 1,
                "CreatedTime": "2020-09-22T00:00:00+00:00",
                "CPU": 1,
                "RdmaIpAddresses": [],
                "CamRoleName": "",
                "PublicIpAddresses": [
                    "123.207.11.190"
                ],
                "Tags": [
                    {
                        "Value": "test",
                        "Key": "test"
                    }
                ],
                "InstanceId": "ins-xlsyru2j",
                "ImageId": "img-8toqc6s3",
                "StopChargingMode": "NOT_APPLICABLE",
                "InstanceChargeType": "POSTPAID_BY_HOUR",
                "InstanceType": "S2.SMALL2",
                "SystemDisk": {
                    "DiskSize": 50,
                    "CdcId": "cdc-xxxxxxxx",
                    "DiskId": "disk-czsodtl1",
                    "DiskType": "CLOUD_SSD"
                },
                "Placement": {
                    "HostId": "host-h3m57oik",
                    "ProjectId": 1174660,
                    "HostIds": [],
                    "Zone": "ap-guangzhou-1",
                    "HostIps": []
                },
                "PrivateIpAddresses": [
                    "172.16.32.78"
                ],
                "OsName": "CentOS 7.4 64bit",
                "SecurityGroupIds": [
                    "sg-p1ezv4wz"
                ],
                "InstanceName": "test",
                "DataDisks": [
                    {
                        "DeleteWithInstance": true,
                        "Encrypt": true,
                        "CdcId": "cdc-xxxxxxxx",
                        "DiskType": "CLOUD_SSD",
                        "ThroughputPerformance": 0,
                        "KmsKeyId": null,
                        "DiskSize": 50,
                        "SnapshotId": null,
                        "DiskId": "disk-bzsodtn1"
                    }
                ],
                "IsolatedSource": "NOTISOLATED",
                "VirtualPrivateCloud": {
                    "SubnetId": "subnet-mv4sn55k",
                    "AsVpcGateway": false,
                    "Ipv6AddressCount": 1,
                    "VpcId": "vpc-m0cnatxj",
                    "PrivateIpAddresses": [
                        "172.16.3.59"
                    ]
                },
                "LatestOperationRequestId": "c7de1287-061d-4ace-8caf-6ad8e5a2f29a",
                "InternetAccessible": {
                    "PublicIpAssigned": true,
                    "InternetChargeType": "TRAFFIC_POSTPAID_BY_HOUR",
                    "InternetMaxBandwidthOut": 1
                },
                "HpcClusterId": "",
                "LatestOperation": "ResetInstancesType"
            }
        ],
        "TotalCount": 2,
        "RequestId": "d655191e-a39d-43d2-8349-8c3f2bf4b327"
    }
}
```

**Example 2: 查询绑定了标签的实例**

查询绑定了标签键值对（city:shenzhen）的实例。

Input: 

```
tccli cvm DescribeInstances --cli-unfold-argument  \
    --Limit 1 \
    --Filters.0.Values shenzhen \
    --Filters.0.Name tag:city \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "InstanceSet": [
            {
                "RenewFlag": "NOTIFY_AND_MANUAL_RENEW",
                "Uuid": "68b510db-b4c1-4630-a62b-73d0c7c970f9",
                "InstanceState": "RUNNING",
                "LatestOperationState": "SUCCESS",
                "OsName": "CentOS 7.6 64bit",
                "CreatedTime": "2020-03-10T02:43:51Z",
                "RestrictState": "NORMAL",
                "ExpiredTime": "2020-04-10T02:47:36Z",
                "DisasterRecoverGroupId": "",
                "Memory": 1,
                "IPv6Addresses": null,
                "CPU": 1,
                "CamRoleName": "",
                "PublicIpAddresses": [
                    "123.207.11.190"
                ],
                "Tags": [
                    {
                        "Value": "shenzhen",
                        "Key": "city"
                    }
                ],
                "InstanceId": "ins-9bxebleo",
                "ImageId": "img-9qabwvbn",
                "StopChargingMode": "NOT_APPLICABLE",
                "InstanceChargeType": "PREPAID",
                "InstanceType": "S1.SMALL1",
                "SystemDisk": {
                    "DiskSize": 50,
                    "DiskId": "disk-nucurerk",
                    "DiskType": "CLOUD_PREMIUM"
                },
                "IsolatedSource": "NOTISOLATED",
                "Placement": {
                    "ProjectId": 1174660,
                    "Zone": "ap-guangzhou-2"
                },
                "PrivateIpAddresses": [
                    "172.16.32.78"
                ],
                "LoginSettings": {
                    "KeyIds": null
                },
                "SecurityGroupIds": [
                    "sg-p1ezv4wz"
                ],
                "DedicatedClusterId": "",
                "InstanceName": "测试实例",
                "DataDisks": [],
                "VirtualPrivateCloud": {
                    "SubnetId": "subnet-a2676p0e",
                    "AsVpcGateway": false,
                    "VpcId": "vpc-g7wzcv7n"
                },
                "LatestOperationRequestId": "3554eb5b-1cfa-471a-ae76-dc436c9d43e8",
                "InternetAccessible": {
                    "InternetMaxBandwidthOut": 1,
                    "InternetChargeType": "BANDWIDTH_PREPAID"
                },
                "RdmaIpAddresses": [],
                "HpcClusterId": "",
                "LatestOperation": "RenewInstances"
            }
        ],
        "TotalCount": 1,
        "RequestId": "62DDFFC6-FDB5-44F7-20A6-59152E3D129A"
    }
}
```

**Example 3: 查询实例的最新操作情况**

当对实例发起 StopInstances 后，通过 DescribeInstances 可以查询到实例的 LatestOperation 为 StopInstances，LatestOperationState 为 OPERATING。

Input: 

```
tccli cvm DescribeInstances --cli-unfold-argument  \
    --Limit 1 \
    --Filters.0.Values ap-guangzhou-2 ap-guangzhou-1 \
    --Filters.0.Name zone \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "InstanceSet": [
            {
                "RenewFlag": "NOTIFY_AND_MANUAL_RENEW",
                "Uuid": "e85f1388-0422-410d-8e50-bef540e78c18",
                "InstanceState": "RUNNING",
                "LatestOperationState": "OPERATING",
                "LoginSettings": {
                    "Password": "123qwe!@#QWE",
                    "KeepImageLogin": "False",
                    "KeyIds": [
                        "skey-b4vakk62"
                    ]
                },
                "IPv6Addresses": [
                    "2001:0db8:86a3:08d3:1319:8a2e:0370:7344"
                ],
                "RestrictState": "PROTECTIVELY_ISOLATED",
                "ExpiredTime": "2020-09-22T00:00:00+00:00",
                "DisasterRecoverGroupId": "ps-xxxxxxxx",
                "Memory": 1,
                "CreatedTime": "2020-09-22T00:00:00+00:00",
                "CPU": 1,
                "RdmaIpAddresses": [],
                "CamRoleName": "",
                "DedicatedClusterId": "",
                "PublicIpAddresses": [
                    "123.207.11.190"
                ],
                "Tags": [
                    {
                        "Value": "test",
                        "Key": "test"
                    }
                ],
                "InstanceId": "ins-xlsyru2j",
                "ImageId": "img-8toqc6s3",
                "StopChargingMode": "NOT_APPLICABLE",
                "InstanceChargeType": "POSTPAID_BY_HOUR",
                "InstanceType": "S2.SMALL2",
                "SystemDisk": {
                    "DiskSize": 50,
                    "CdcId": "cdc-xxxxxxxx",
                    "DiskId": "disk-czsodtl1",
                    "DiskType": "CLOUD_SSD"
                },
                "Placement": {
                    "HostId": "host-h3m57oik",
                    "ProjectId": 1174660,
                    "HostIds": [],
                    "Zone": "ap-guangzhou-1",
                    "HostIps": []
                },
                "PrivateIpAddresses": [
                    "172.16.32.78"
                ],
                "OsName": "CentOS 7.4 64bit",
                "SecurityGroupIds": [
                    "sg-p1ezv4wz"
                ],
                "InstanceName": "test",
                "DataDisks": [
                    {
                        "DeleteWithInstance": true,
                        "Encrypt": true,
                        "CdcId": "cdc-xxxxxxxx",
                        "DiskType": "CLOUD_SSD",
                        "ThroughputPerformance": 0,
                        "KmsKeyId": null,
                        "DiskSize": 50,
                        "SnapshotId": null,
                        "DiskId": "disk-bzsodtn1"
                    }
                ],
                "IsolatedSource": "NOTISOLATED",
                "VirtualPrivateCloud": {
                    "SubnetId": "subnet-mv4sn55k",
                    "AsVpcGateway": false,
                    "Ipv6AddressCount": 1,
                    "VpcId": "vpc-m0cnatxj",
                    "PrivateIpAddresses": [
                        "172.16.3.59"
                    ]
                },
                "LatestOperationRequestId": "c7de1287-061d-4ace-8caf-6ad8e5a2f29a",
                "InternetAccessible": {
                    "PublicIpAssigned": true,
                    "InternetChargeType": "TRAFFIC_POSTPAID_BY_HOUR",
                    "InternetMaxBandwidthOut": 1
                },
                "HpcClusterId": "",
                "LatestOperation": "StopInstances"
            }
        ],
        "TotalCount": 2,
        "RequestId": "d655191e-a39d-43d2-8349-8c3f2bf4b327"
    }
}
```

