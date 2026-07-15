**Example 1: 按实例ID查询**



Input: 

```
tccli lighthouse DescribeAccountInstancesInternal --cli-unfold-argument  \
    --Filters.0.Name instance-id \
    --Filters.0.Values lhins-bjmss2v3 \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "AccountInstanceSet": [
            {
                "AccountAppId": 200000004,
                "AccountOriginAppId": 200000008,
                "AccountUin": "7******9",
                "BlueprintId": "lhbp-qnuz61zs",
                "BlueprintImageUrl": "https://cloudcache.tencent-cloud.com/open_proj/proj_qcloud_v2/tc-console/tea-static-lighthouse/src/styles/slice/Ubuntu.svg",
                "BlueprintName": "ubuntu22",
                "BundleId": "bundle_starter_mc_med2_01",
                "CPU": 2,
                "CreatedTime": "2026-06-03T08:14:44Z",
                "DisplayArea": "NORMAL",
                "ExpiredTime": "2026-06-03T08:17:50Z",
                "InitInvocationId": "inv-w2dwrtg923",
                "InstanceChargeType": "PREPAID",
                "InstanceId": "lhins-bjmss2v3",
                "InstanceName": "Ubuntu-zguO",
                "InstanceRestrictState": "NORMAL",
                "InstanceState": "SHUTDOWN",
                "InternetAccessible": {
                    "InternetChargeType": "TRAFFIC_POSTPAID_BY_HOUR",
                    "InternetMaxBandwidthOut": 3,
                    "PublicIpAssigned": true,
                    "PublicIpv4MaxBandwidthOut": 3,
                    "PublicIpv6MaxBandwidthOut": 3
                },
                "IsolatedTime": "2026-06-03T08:17:50Z",
                "LatestOperation": "IsolateInstances",
                "LatestOperationRequestId": "20cd17d2-08ec-42b4-afb0-a0633ec231aa",
                "LatestOperationStartedTime": "2026-06-03T08:17:53Z",
                "LatestOperationState": "SUCCESS",
                "LoginSettings": {
                    "KeyIds": []
                },
                "Memory": 2,
                "OriginInstanceId": "ins-kr4214a4",
                "OsName": "Ubuntu Server 22.04 LTS 64bit",
                "Platform": "UBUNTU",
                "PlatformType": "LINUX_UNIX",
                "PrivateAddresses": [
                    "10.1.0.2"
                ],
                "PublicAddresses": [
                    "1.14.57.245"
                ],
                "PublicIpv6Addresses": [
                    "A35D:4086:0D5E:F690:9091:32CF:D262:420C"
                ],
                "PurchaseSource": "MC",
                "Region": "ap-guangzhou",
                "RenewFlag": "NOTIFY_AND_AUTO_RENEW",
                "SubAccountUin": "75092499",
                "SupportIpv6Detail": {
                    "Detail": "HAD_BEEN_ASSIGNED",
                    "IsSupport": false,
                    "Message": "The current instance has been assigned an IPv6 address."
                },
                "SystemDisk": {
                    "DiskId": "lhdisk-hfybvhul",
                    "DiskSize": 40,
                    "DiskType": "CLOUD_SSD"
                },
                "Tags": [],
                "Uuid": "c9b4e6a1-df4c-484b-8878-57196870b560",
                "VpcId": "vpc-e3avu0el",
                "Zone": "ap-guangzhou-2"
            }
        ],
        "TotalCount": 1,
        "RequestId": "2ed2d2a1-b9cf-43a6-9a29-7839eb039d03"
    }
}
```

