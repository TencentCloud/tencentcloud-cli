**Example 1: Querying a list of instances**

This example shows you how to query instances in Guangzhou Zone 1 or Guangzhou Zone 2 and return up to one result.

Input: 

```
tccli cvm DescribeInstances --cli-unfold-argument  \
    --Filters.0.Name zone \
    --Filters.0.Values ap-guangzhou-1 ap-guangzhou-2 \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "InstanceSet": [
            {
                "RenewFlag": "null",
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
                "Tags": [],
                "InstanceId": "ins-9bxebleo",
                "PhysicalPosition": {
                    "PosId": "48C7C7A369705E6F3FE45126D39F2915",
                    "SwitchId": "A5A6ACC7CB106C396E3CF7477C883FB4",
                    "RackId": "DFE8AC9E645197818BE0B55AEAF0DD17"
                },
                "ImageId": "img-9qabwvbn",
                "StopChargingMode": "NOT_APPLICABLE",
                "InstanceChargeType": "PREPAID",
                "InstanceType": "S1.SMALL1",
                "SystemDisk": {
                    "DiskSize": 50,
                    "DiskId": "disk-nucurerk",
                    "DiskType": "CLOUD_PREMIUM"
                },
                "Placement": {
                    "ProjectId": 1174660,
                    "HostId": null,
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
                "InstanceName": "Test instance",
                "DataDisks": null,
                "IsolatedSource": "NOTISOLATED",
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
                "LatestOperation": "RenewInstances"
            }
        ],
        "TotalCount": 2,
        "RequestId": "62DDFFC6-FDB5-44F7-20A6-59152E3D129A"
    }
}
```

**Example 2: Querying the latest operation of an instance**

This example shows you how to use DescribeInstances to query the last operation and status of an instance after using StopInstances to stop it. You will see that the value of `LatestOperation` is `StopInstances` and `LatestOperationState` is `OPERATING`.

Input: 

```
tccli cvm DescribeInstances --cli-unfold-argument  \
    --Filters.0.Name zone \
    --Filters.0.Values ap-guangzhou-1 ap-guangzhou-2 \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "InstanceSet": [
            {
                "RenewFlag": "null",
                "Uuid": "68b510db-b4c1-4630-a62b-73d0c7c970f9",
                "InstanceState": "STOPPING",
                "LatestOperationState": "OPERATING",
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
                "Tags": [],
                "InstanceId": "ins-9bxebleo",
                "PhysicalPosition": {
                    "PosId": "48C7C7A369705E6F3FE45126D39F2915",
                    "SwitchId": "A5A6ACC7CB106C396E3CF7477C883FB4",
                    "RackId": "DFE8AC9E645197818BE0B55AEAF0DD17"
                },
                "ImageId": "img-9qabwvbn",
                "StopChargingMode": "NOT_APPLICABLE",
                "InstanceChargeType": "PREPAID",
                "InstanceType": "S1.SMALL1",
                "SystemDisk": {
                    "DiskSize": 50,
                    "DiskId": "disk-nucurerk",
                    "DiskType": "CLOUD_PREMIUM"
                },
                "Placement": {
                    "ProjectId": 1174660,
                    "HostId": null,
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
                "InstanceName": "Test instance",
                "DataDisks": null,
                "IsolatedSource": "NOTISOLATED",
                "VirtualPrivateCloud": {
                    "SubnetId": "subnet-a2676p0e",
                    "AsVpcGateway": false,
                    "VpcId": "vpc-g7wzcv7n"
                },
                "LatestOperationRequestId": "2f8decef-78b2-4e20-bcfe-7a5112658a05",
                "InternetAccessible": {
                    "InternetMaxBandwidthOut": 1,
                    "InternetChargeType": "BANDWIDTH_PREPAID"
                },
                "LatestOperation": "StopInstances"
            }
        ],
        "TotalCount": 2,
        "RequestId": "62DDFFC6-FDB5-44F7-20A6-59152E3D129A"
    }
}
```

**Example 3: Querying instances associated with a tag**

This example shows you how to query a list of instances associated with the tag key-value pair `city:shenzhen`.

Input: 

```
tccli cvm DescribeInstances --cli-unfold-argument  \
    --Filters.0.Name tag:city \
    --Filters.0.Values shenzhen \
    --Offset 0 \
    --Limit 1
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
                        "tagKey": "city",
                        "Value": "shenzhen",
                        "tagValue": "shenzhen",
                        "Key": "city"
                    }
                ],
                "InstanceId": "ins-9bxebleo",
                "PhysicalPosition": {
                    "PosId": "48C7C7A369705E6F3FE45126D39F2915",
                    "SwitchId": "A5A6ACC7CB106C396E3CF7477C883FB4",
                    "RackId": "DFE8AC9E645197818BE0B55AEAF0DD17"
                },
                "ImageId": "img-9qabwvbn",
                "StopChargingMode": "NOT_APPLICABLE",
                "InstanceChargeType": "PREPAID",
                "InstanceType": "S1.SMALL1",
                "SystemDisk": {
                    "DiskSize": 50,
                    "DiskId": "disk-nucurerk",
                    "DiskType": "CLOUD_PREMIUM"
                },
                "Placement": {
                    "ProjectId": 1174660,
                    "HostId": null,
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
                "InstanceName": "Test instance",
                "DataDisks": null,
                "IsolatedSource": "NOTISOLATED",
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
                "LatestOperation": "RenewInstances"
            }
        ],
        "TotalCount": 1,
        "RequestId": "62DDFFC6-FDB5-44F7-20A6-59152E3D129A"
    }
}
```

