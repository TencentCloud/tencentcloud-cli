**Example 1: 查看实例列表**

限制返回结果最多为一项

Input: 

```
tccli lighthouse DescribeInstances --cli-unfold-argument  \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "InstanceSet": [
            {
                "InstanceId": "lhins-ruy9d2tw",
                "BundleId": "bundle_bw_small1_1",
                "BlueprintId": "lhbp-5e8807lo",
                "Zone": "ap-guangzhou-3",
                "CPU": 1,
                "Memory": 1,
                "InstanceName": "lighthouse-test",
                "OsName": "CentOS 7.6 64bit",
                "Platform": "CENTOS",
                "PlatformType": "LINUX_UNIX",
                "InstanceChargeType": "PREPAID",
                "SystemDisk": {
                    "DiskType": "CLOUD_PREMIUM",
                    "DiskSize": 50,
                    "DiskId": "lhdisk-gayq6kyd"
                },
                "PrivateAddresses": [
                    "10.0.0.5"
                ],
                "PublicAddresses": [
                    "170.106.15.201"
                ],
                "InternetAccessible": {
                    "InternetChargeType": "TRAFFIC_POSTPAID_BY_HOUR",
                    "InternetMaxBandwidthOut": 20,
                    "PublicIpAssigned": true
                },
                "RenewFlag": "NOTIFY_AND_MANUAL_RENEW",
                "LoginSettings": {
                    "KeyIds": []
                },
                "Tags": [
                    {
                        "Key": "lighthouse",
                        "Value": "great"
                    }
                ],
                "InstanceState": "RUNNING",
                "InstanceRestrictState": "NORMAL",
                "Uuid": "1322d32a-2641-45f3-a244-559405b32228",
                "LatestOperation": "StartInstances",
                "LatestOperationState": "SUCCESS",
                "LatestOperationRequestId": "6b9a6dac-888a-4b4d-9739-0d0b66cbfa88",
                "CreatedTime": "2020-04-28T03:46:09Z",
                "ExpiredTime": "2020-05-28T03:46:09Z",
                "IsolatedTime": null
            }
        ],
        "RequestId": "c9aa9e9b-bb2b-4390-b8da-fc976ffc4608"
    }
}
```

