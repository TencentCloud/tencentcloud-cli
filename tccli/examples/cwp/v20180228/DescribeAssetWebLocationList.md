**Example 1: 获取Web站点列表**



Input: 

```
tccli cwp DescribeAssetWebLocationList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Total": 1,
        "Locations": [
            {
                "Uuid": "24c9be55-c743-4a75-a5c7-2a2912341234",
                "Quuid": "24c9be55-c743-4a75-a5c7-2a2912341234",
                "MachineIp": "10.0.0.11",
                "MachineWanIp": "110.84.0.11",
                "MachineName": "test-name",
                "OsInfo": "CentOs Bit64",
                "Name": "test-name",
                "Port": "22",
                "Proto": "tcp",
                "ServiceType": "abc",
                "PathCount": 1,
                "User": "root",
                "MainPath": "/root",
                "MainPathOwner": "/root",
                "Permission": "abc",
                "ProjectId": 1,
                "Tag": [
                    {
                        "Rid": 0,
                        "Name": "test-name",
                        "TagId": 1
                    }
                ],
                "Id": "abc",
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
                }
            }
        ],
        "RequestId": "37b6df34-68f1-4ab8-a3d8-7b89de604c82"
    }
}
```

