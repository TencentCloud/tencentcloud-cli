**Example 1: 查询实例信息**

查询实例信息

Input: 

```
tccli lighthouse DescribeAccountInstances --cli-unfold-argument  \
    --Filters.0.Name instance-id \
    --Filters.0.Values lhins-bgkzhuwp \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "AccountInstanceSet": [
            {
                "AccountOriginAppId": 251019999,
                "AccountAppId": 251236960,
                "AccountUin": "700000565983",
                "Region": "ap-guangzhou",
                "BlueprintName": "debian",
                "OsName": "Debian 10.2 64bit",
                "InstanceId": "lhins-bgkzhuwp",
                "BundleId": "bundle2022_gen_01",
                "BlueprintId": "lhbp-8l0svqtk",
                "Zone": "ap-guangzhou-4",
                "CPU": 2,
                "Memory": 2,
                "InstanceName": "Debian-R19p",
                "Platform": "DEBIAN",
                "PlatformType": "LINUX_UNIX",
                "InstanceChargeType": "PREPAID",
                "SystemDisk": {
                    "DiskType": "CLOUD_SSD",
                    "DiskSize": 40,
                    "DiskId": "lhdisk-5s28cknn"
                },
                "PrivateAddresses": [
                    "10.0.5.5"
                ],
                "PublicAddresses": [
                    "123.207.2.219"
                ],
                "InternetAccessible": {
                    "InternetChargeType": "TRAFFIC_POSTPAID_BY_HOUR",
                    "InternetMaxBandwidthOut": 4,
                    "PublicIpAssigned": true
                },
                "RenewFlag": "NOTIFY_AND_MANUAL_RENEW",
                "LoginSettings": {
                    "KeyIds": []
                },
                "InstanceState": "RUNNING",
                "InstanceRestrictState": "NORMAL",
                "Uuid": "4274453f-9f1b-4c2b-a35d-759530dd47a8",
                "Tags": [],
                "LatestOperation": "",
                "LatestOperationState": "",
                "LatestOperationRequestId": "",
                "CreatedTime": "2023-05-26T08:49:56Z",
                "ExpiredTime": "2023-06-26T08:49:56Z",
                "IsolatedTime": null,
                "BlueprintImageUrl": "",
                "VpcId": "vpc-auk9c3lx"
            }
        ],
        "RequestId": "efca6489-c9ba-4e50-b604-bc190cdbe21d"
    }
}
```

