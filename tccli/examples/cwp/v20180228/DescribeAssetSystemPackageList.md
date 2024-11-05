**Example 1: 获取资产管理系统安装包列表**

获取资产管理系统安装包列表

Input: 

```
tccli cwp DescribeAssetSystemPackageList --cli-unfold-argument  \
    --Limit 1 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "Packages": [
            {
                "Name": "test-name",
                "Desc": "idesc",
                "Version": "0.1.1",
                "InstallTime": "2024-10-11 12:23:34",
                "Type": "Web",
                "MachineName": "test-name",
                "MachineIp": "10.0.0.11",
                "OsInfo": "CentOs Bit64",
                "UpdateTime": "2024-10-11 12:23:34",
                "FirstTime": "2024-10-11 12:23:34",
                "IsNew": 0,
                "MachineExtraInfo": {
                    "WanIP": "110.84.0.11",
                    "PrivateIP": "10.0.0.11",
                    "NetworkType": 0,
                    "NetworkName": "vpc-12341234",
                    "InstanceID": "ins-aj28fjz",
                    "HostName": "test-name"
                },
                "Quuid": "24c9be55-c743-4a75-a5c7-2a2912341234",
                "Uuid": "24c9be55-c743-4a75-a5c7-2a2912341234"
            }
        ],
        "RequestId": "37b6df34-68f1-4ab8-a3d8-7b89de604c82"
    }
}
```

