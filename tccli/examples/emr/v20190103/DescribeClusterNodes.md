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
            "HOST",
            "MNode",
            "POD"
        ],
        "NodeList": [
            {
                "AppId": 1258469122,
                "ApplyTime": "2024-11-05 20:40:30",
                "AutoFlag": 0,
                "CdbIp": "",
                "CdbNodeInfo": null,
                "CdbPort": 0,
                "ChargeType": 0,
                "Clients": "HDFS,YARN,ZOOKEEPER,FILEBEAT,RUNTIME",
                "CpuNum": 4,
                "CurrentTime": "2024-11-05 20:44:07",
                "Destroyable": 0,
                "DeviceClass": "VSELF_5",
                "DeviceName": "EMR标准型S5",
                "DisableApiTermination": false,
                "DiskSize": "200.00 GB",
                "DynamicPodSpec": "",
                "EmrResourceId": "emr-vm-3ep60g79",
                "ExpireTime": "0000-00-00 00:00:00",
                "Flag": 2,
                "FreeTime": "0000-00-00 00:00:00",
                "HardwareResourceType": "HOST",
                "HwDiskSize": 214748364800,
                "HwDiskSizeDesc": "200.00 GB",
                "HwMemSize": 8589934592,
                "HwMemSizeDesc": "8GB",
                "Ip": "10.233.179.208",
                "IsAutoRenew": 1,
                "IsDynamicSpec": 0,
                "IsFederation": 0,
                "MCMultiDisk": [
                    {
                        "Count": 1,
                        "Type": 4,
                        "Volume": 214748364800
                    }
                ],
                "MemDesc": "8GB",
                "MemSize": 8589934592,
                "Mutable": 1,
                "NameTag": "core.0",
                "OrderNo": "ins-79jcgj7m",
                "RegionId": 1,
                "Remark": "",
                "RootSize": 70,
                "RootStorageType": 4,
                "SerialNo": "240606f1-dc72-4760-958f-3d11b7430c9f",
                "ServiceClient": "",
                "Services": "DataNode,Filebeat,NodeManager,Sysctl",
                "ServicesStatus": "DataNode:STARTED,Filebeat:STARTED,NodeManager:STARTED,Sysctl:STARTED",
                "SharedClusterId": "",
                "SharedClusterIdDesc": "",
                "Spec": "CVM.S5",
                "StorageType": 4,
                "SubnetInfo": {
                    "SubnetId": "subnet-ax8z9f1u",
                    "SubnetName": "vigo-subnet"
                },
                "SupportModifyPayMode": 0,
                "Tags": [],
                "TradeVersion": 1,
                "WanIp": "",
                "Zone": "ap-guangzhou-3",
                "ZoneId": 100003
            },
            {
                "AppId": 1258469122,
                "ApplyTime": "2024-11-05 20:40:30",
                "AutoFlag": 0,
                "CdbIp": "",
                "CdbNodeInfo": null,
                "CdbPort": 0,
                "ChargeType": 0,
                "Clients": "HDFS,YARN,ZOOKEEPER,FILEBEAT,RUNTIME",
                "CpuNum": 4,
                "CurrentTime": "2024-11-05 20:44:07",
                "Destroyable": 0,
                "DeviceClass": "VSELF_5",
                "DeviceName": "EMR标准型S5",
                "DisableApiTermination": false,
                "DiskSize": "200.00 GB",
                "DynamicPodSpec": "",
                "EmrResourceId": "emr-vm-az843bs9",
                "ExpireTime": "0000-00-00 00:00:00",
                "Flag": 2,
                "FreeTime": "0000-00-00 00:00:00",
                "HardwareResourceType": "HOST",
                "HwDiskSize": 214748364800,
                "HwDiskSizeDesc": "200.00 GB",
                "HwMemSize": 8589934592,
                "HwMemSizeDesc": "8GB",
                "Ip": "10.233.179.138",
                "IsAutoRenew": 1,
                "IsDynamicSpec": 0,
                "IsFederation": 0,
                "MCMultiDisk": [
                    {
                        "Count": 1,
                        "Type": 4,
                        "Volume": 214748364800
                    }
                ],
                "MemDesc": "8GB",
                "MemSize": 8589934592,
                "Mutable": 1,
                "NameTag": "core.1",
                "OrderNo": "ins-aodlsfs2",
                "RegionId": 1,
                "Remark": "",
                "RootSize": 70,
                "RootStorageType": 4,
                "SerialNo": "a167d792-3f7d-4927-bc64-70604b4172d2",
                "ServiceClient": "",
                "Services": "DataNode,Filebeat,NodeManager,Sysctl",
                "ServicesStatus": "DataNode:STARTED,Filebeat:STARTED,NodeManager:STARTED,Sysctl:STARTED",
                "SharedClusterId": "",
                "SharedClusterIdDesc": "",
                "Spec": "CVM.S5",
                "StorageType": 4,
                "SubnetInfo": {
                    "SubnetId": "subnet-ax8z9f1u",
                    "SubnetName": "vigo-subnet"
                },
                "SupportModifyPayMode": 0,
                "Tags": [],
                "TradeVersion": 1,
                "WanIp": "",
                "Zone": "ap-guangzhou-3",
                "ZoneId": 100003
            },
            {
                "AppId": 1258469122,
                "ApplyTime": "2024-11-05 20:40:30",
                "AutoFlag": 0,
                "CdbIp": "",
                "CdbNodeInfo": null,
                "CdbPort": 0,
                "ChargeType": 0,
                "Clients": "HDFS,YARN,ZOOKEEPER,OPENLDAP,KNOX,FILEBEAT,RUNTIME",
                "CpuNum": 8,
                "CurrentTime": "2024-11-05 20:44:07",
                "Destroyable": 0,
                "DeviceClass": "VSELF_5",
                "DeviceName": "EMR标准型S5",
                "DisableApiTermination": false,
                "DiskSize": "200.00 GB",
                "DynamicPodSpec": "",
                "EmrResourceId": "emr-vm-7sgwp92l",
                "ExpireTime": "0000-00-00 00:00:00",
                "Flag": 1,
                "FreeTime": "0000-00-00 00:00:00",
                "HardwareResourceType": "HOST",
                "HwDiskSize": 214748364800,
                "HwDiskSizeDesc": "200.00 GB",
                "HwMemSize": 17179869184,
                "HwMemSizeDesc": "16GB",
                "Ip": "10.233.179.87",
                "IsAutoRenew": 1,
                "IsDynamicSpec": 0,
                "IsFederation": 0,
                "MCMultiDisk": [
                    {
                        "Count": 1,
                        "Type": 4,
                        "Volume": 214748364800
                    }
                ],
                "MemDesc": "16GB",
                "MemSize": 17179869184,
                "Mutable": 1,
                "NameTag": "master.0",
                "OrderNo": "ins-olrawbba",
                "RegionId": 1,
                "Remark": "",
                "RootSize": 70,
                "RootStorageType": 4,
                "SerialNo": "b8f36fdb-7f78-402e-ace6-63b3d3f277fd",
                "ServiceClient": "",
                "Services": "Filebeat,gateway,JobHistoryServer,ldap,NameNode,Zookeeper,ResourceManager,slapd,Sysctl,TimeLineServer",
                "ServicesStatus": "Filebeat:STARTED,gateway:STARTED,JobHistoryServer:STARTED,ldap:STARTED,NameNode:STARTED,Zookeeper:STARTED,ResourceManager:STARTED,slapd:STARTED,Sysctl:STARTED,TimeLineServer:STARTED",
                "SharedClusterId": "",
                "SharedClusterIdDesc": "",
                "Spec": "CVM.S5",
                "StorageType": 4,
                "SubnetInfo": {
                    "SubnetId": "subnet-ax8z9f1u",
                    "SubnetName": "vigo-subnet"
                },
                "SupportModifyPayMode": 0,
                "Tags": [],
                "TradeVersion": 1,
                "WanIp": "0.0.0.0",
                "Zone": "ap-guangzhou-3",
                "ZoneId": 100003
            }
        ],
        "RequestId": "ee21e3bd-2340-4501-b63c-2edbcff0f220",
        "TagKeys": null,
        "TotalCnt": 3
    }
}
```

