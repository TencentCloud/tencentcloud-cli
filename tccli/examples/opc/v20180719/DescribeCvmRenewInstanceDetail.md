**Example 1: 获取新购CVM的信息，用于续费场景**

获取新购CVM的信息，用于续费场景

Input: 

```
tccli opc DescribeCvmRenewInstanceDetail --cli-unfold-argument  \
    --GoodsId 12616
```

Output: 
```
{
    "Response": {
        "InstanceDetail": {
            "AddTimeStamp": "2019-11-22 18:01:24",
            "Alias": "部署",
            "AppId": 1300674097,
            "ApplicationRole": "",
            "AutoRenewFlag": 0,
            "Bandwidth": 200,
            "BillId": null,
            "Cpu": 4,
            "CustomId": 1,
            "CvmPayMode": 1,
            "Deadline": "2020-11-22 18:01:24",
            "DeviceAssetId": "C4e46f48-b06b-4277-8248-8687a86cffa6",
            "DeviceClass": "VSELF4",
            "DeviceClassFlag": 0,
            "DeviceId": 682248220,
            "DeviceImageId": 0,
            "DeviceLanIp": "172.17.0.11",
            "DeviceWanIp": "106.54.180.250",
            "Disk": 0,
            "DiskType": 6,
            "ErrorCode": 0,
            "ErrorKey": null,
            "Fpga": 0,
            "Gpu": 0,
            "HypervisorUpdateFlag": 0,
            "IdcName": "上海腾讯宝信DC电信7号楼M1-2-3",
            "IsSafeIsolated": 0,
            "IsVpcGateway": 0,
            "IsolateTime": "0000-00-00 00:00:00",
            "IspName": "腾讯CAP",
            "ItemId": 0,
            "LastOperation": "",
            "LatestOperation": "ResetInstancesPassword",
            "LatestOperationState": "SUCCESS",
            "LocalEthDev": "Eth0",
            "Mem": 8,
            "NetworkPayMode": 2,
            "OsName": "Centos7.6.0X64",
            "ProjectId": 0,
            "RecycleFlag": 0,
            "RegionId": 4,
            "RootSize": 50,
            "RootType": 6,
            "Runflag": 0,
            "SafeIsolatedInfo": "",
            "State": "RUNNING",
            "Status": 1,
            "SubnetId": 872305,
            "SwapSize": 0,
            "TmpDeviceId": 12753981,
            "UHostId": null,
            "UInstanceId": "Ins-05q7204t",
            "UpdateTimestamp": "2019-11-22 18:02:29",
            "Uuid": "A01e4412-b315-409e-b891-445d3018a0d0",
            "VpcId": 2897064,
            "ZoneId": 200002,
            "ZoneName": "上海二区"
        },
        "RequestId": "e4ce770c-66ea-4917-b533-6884774788d5"
    }
}
```

