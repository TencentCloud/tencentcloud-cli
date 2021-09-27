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
                "OsInfo": "xx",
                "ServiceType": "xx",
                "PathCount": 1,
                "MachineWanIp": "xx",
                "Uuid": "xx",
                "MainPathOwner": "xx",
                "Proto": "xx",
                "MachineName": "xx",
                "Permission": "xx",
                "Port": 1,
                "MainPath": "xx",
                "Tag": [
                    {
                        "TagId": 1,
                        "Rid": 0,
                        "Name": "xx"
                    }
                ],
                "Quuid": "xx",
                "ProjectId": 1,
                "User": "xx",
                "MachineIp": "xx",
                "Name": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

