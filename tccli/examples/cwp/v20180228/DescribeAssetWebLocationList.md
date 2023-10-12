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
                "Uuid": "abc",
                "Quuid": "abc",
                "MachineIp": "abc",
                "MachineWanIp": "abc",
                "MachineName": "abc",
                "OsInfo": "abc",
                "Name": "abc",
                "Port": "abc",
                "Proto": "abc",
                "ServiceType": "abc",
                "PathCount": 1,
                "User": "abc",
                "MainPath": "abc",
                "MainPathOwner": "abc",
                "Permission": "abc",
                "ProjectId": 1,
                "Tag": [
                    {
                        "Rid": 0,
                        "Name": "abc",
                        "TagId": 1
                    }
                ],
                "Id": "abc",
                "UpdateTime": "abc",
                "FirstTime": "abc",
                "IsNew": 0,
                "MachineExtraInfo": {
                    "WanIP": "abc",
                    "PrivateIP": "abc",
                    "NetworkType": 0,
                    "NetworkName": "abc",
                    "InstanceID": "abc",
                    "HostName": "abc"
                }
            }
        ],
        "RequestId": "abc"
    }
}
```

