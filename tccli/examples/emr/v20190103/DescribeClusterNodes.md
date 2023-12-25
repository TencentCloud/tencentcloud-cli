**Example 1: 获取硬件节点信息**

通过emr集群ID获取硬件节点信息

Input: 

```
tccli emr DescribeClusterNodes --cli-unfold-argument  \
    --InstanceId emr-6deluvd4 \
    --NodeFlag all \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCnt": 0,
        "NodeList": [
            {
                "AppId": 0,
                "SerialNo": "abc",
                "OrderNo": "abc",
                "WanIp": "abc",
                "Flag": 0,
                "Spec": "abc",
                "CpuNum": 0,
                "MemSize": 0,
                "MemDesc": "abc",
                "RegionId": 0,
                "ZoneId": 0,
                "ApplyTime": "abc",
                "FreeTime": "abc",
                "DiskSize": "abc",
                "NameTag": "abc",
                "Services": "abc",
                "StorageType": 0,
                "RootSize": 0,
                "ChargeType": 0,
                "CdbIp": "abc",
                "CdbPort": 0,
                "HwDiskSize": 0,
                "HwDiskSizeDesc": "abc",
                "HwMemSize": 0,
                "HwMemSizeDesc": "abc",
                "ExpireTime": "abc",
                "EmrResourceId": "abc",
                "IsAutoRenew": 0,
                "DeviceClass": "abc",
                "Mutable": 0,
                "MCMultiDisk": [
                    {
                        "Type": 0,
                        "Volume": 0,
                        "Count": 0
                    }
                ],
                "CdbNodeInfo": {
                    "InstanceName": "abc",
                    "Ip": "abc",
                    "Port": 0,
                    "MemSize": 0,
                    "Volume": 0,
                    "Service": "abc",
                    "ExpireTime": "abc",
                    "ApplyTime": "abc",
                    "PayType": 0,
                    "ExpireFlag": true,
                    "Status": 0,
                    "IsAutoRenew": 0,
                    "SerialNo": "abc",
                    "ZoneId": 0,
                    "RegionId": 0
                },
                "Ip": "abc",
                "Destroyable": 0,
                "Tags": [
                    {
                        "TagKey": "abc",
                        "TagValue": "abc"
                    }
                ],
                "AutoFlag": 0,
                "HardwareResourceType": "abc",
                "IsDynamicSpec": 0,
                "DynamicPodSpec": "abc",
                "SupportModifyPayMode": 0,
                "RootStorageType": 0,
                "Zone": "abc",
                "SubnetInfo": {
                    "SubnetName": "abc",
                    "SubnetId": "abc"
                },
                "Clients": "abc",
                "CurrentTime": "abc",
                "IsFederation": 0,
                "DeviceName": "abc",
                "ServiceClient": "abc",
                "DisableApiTermination": true,
                "TradeVersion": 0,
                "ServicesStatus": "abc"
            }
        ],
        "TagKeys": [
            "abc"
        ],
        "HardwareResourceTypeList": [
            "abc"
        ],
        "RequestId": "abc"
    }
}
```

