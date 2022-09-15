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
        "HardwareResourceTypeList": [
            "all"
        ],
        "NodeList": [
            {
                "AppId": 251008830,
                "ApplyTime": "2020-02-24 20:31:06",
                "CdbIp": "",
                "CdbNodeInfo": null,
                "CdbPort": 0,
                "ChargeType": 0,
                "CpuNum": 8,
                "Destroyable": 0,
                "DeviceClass": "VSELF_2",
                "DiskSize": "100.00 GB",
                "EmrResourceId": "emr-vm-6xyf2cb2",
                "ExpireTime": "0000-00-00 00:00:00",
                "Flag": 1,
                "FreeTime": "0000-00-00 00:00:00",
                "HwDiskSize": 107374182400,
                "HwDiskSizeDesc": "100.00 GB",
                "HwMemSize": 17179869184,
                "HwMemSizeDesc": "16GB",
                "Ip": "10.0.0.76",
                "IsAutoRenew": 0,
                "MCMultiDisk": [
                    {
                        "Count": 1,
                        "Type": 5,
                        "Volume": 107374182400
                    }
                ],
                "MemDesc": "16GB",
                "MemSize": 17179869184,
                "Mutable": 1,
                "NameTag": "master.0",
                "OrderNo": "ins-20224atg",
                "RegionId": 1,
                "RootSize": 0,
                "SerialNo": "83d977e5-fa68-4051-875e-ad30ff42534f",
                "Services": "Zookeeper,NameNode,ResourceManager,JobHistoryServer,HMaster,HbaseThrift,HiveServer2,HiveMetaStore,HiveWebHcat,Spark,SparkJobHistoryServer,Presto-Coordinator,knox",
                "Spec": "CVM.S2",
                "StorageType": 5,
                "Tags": [],
                "WanIp": "--",
                "ZoneId": 100002,
                "SupportModifyPayMode": 1
            },
            {
                "AppId": 251008830,
                "ApplyTime": "2020-02-24 20:31:07",
                "CdbIp": "",
                "CdbNodeInfo": null,
                "CdbPort": 0,
                "ChargeType": 0,
                "CpuNum": 8,
                "Destroyable": 0,
                "DeviceClass": "VSELF_2",
                "DiskSize": "100.00 GB",
                "EmrResourceId": "emr-vm-cinlo2wc",
                "ExpireTime": "0000-00-00 00:00:00",
                "Flag": 2,
                "FreeTime": "0000-00-00 00:00:00",
                "HwDiskSize": 107374182400,
                "HwDiskSizeDesc": "100.00 GB",
                "HwMemSize": 17179869184,
                "HwMemSizeDesc": "16GB",
                "Ip": "10.0.0.33",
                "IsAutoRenew": 0,
                "MCMultiDisk": [
                    {
                        "Count": 1,
                        "Type": 5,
                        "Volume": 107374182400
                    }
                ],
                "MemDesc": "16GB",
                "MemSize": 17179869184,
                "Mutable": 1,
                "NameTag": "core.0",
                "OrderNo": "ins-20224gpk",
                "RegionId": 1,
                "RootSize": 0,
                "SerialNo": "8ded940b-a579-4c81-be75-3aaf62137337",
                "Services": "DataNode,NodeManager,RegionServer,Presto-Worker",
                "Spec": "CVM.S2",
                "StorageType": 5,
                "Tags": [],
                "WanIp": "",
                "ZoneId": 100002,
                "SupportModifyPayMode": 0
            },
            {
                "AppId": 251008830,
                "ApplyTime": "2020-02-24 20:31:08",
                "CdbIp": "",
                "CdbNodeInfo": null,
                "CdbPort": 0,
                "ChargeType": 0,
                "CpuNum": 8,
                "Destroyable": 0,
                "DeviceClass": "VSELF_2",
                "DiskSize": "100.00 GB",
                "EmrResourceId": "emr-vm-b32qad6s",
                "ExpireTime": "0000-00-00 00:00:00",
                "Flag": 2,
                "FreeTime": "0000-00-00 00:00:00",
                "HwDiskSize": 107374182400,
                "HwDiskSizeDesc": "100.00 GB",
                "HwMemSize": 17179869184,
                "HwMemSizeDesc": "16GB",
                "Ip": "10.0.0.111",
                "IsAutoRenew": 0,
                "MCMultiDisk": [
                    {
                        "Count": 1,
                        "Type": 5,
                        "Volume": 107374182400
                    }
                ],
                "MemDesc": "16GB",
                "MemSize": 17179869184,
                "Mutable": 1,
                "NameTag": "core.1",
                "OrderNo": "ins-202241if",
                "RegionId": 1,
                "RootSize": 0,
                "SerialNo": "c045bcd7-571a-4c64-b0a5-9024c94d5c15",
                "Services": "DataNode,NodeManager,RegionServer,Presto-Worker",
                "Spec": "CVM.S2",
                "StorageType": 5,
                "Tags": [],
                "WanIp": "",
                "ZoneId": 100002,
                "SupportModifyPayMode": 0
            }
        ],
        "RequestId": "bb22bafb-d2a4-4a02-879f-6ccf54a27892",
        "TagKeys": [
            "测试一下",
            "alex_test",
            "beckwuxingjia",
            "ghghghg",
            "tag_auth_test",
            "test",
            "beckwu",
            "emr",
            "lg",
            "bk"
        ],
        "TotalCnt": 3
    }
}
```

