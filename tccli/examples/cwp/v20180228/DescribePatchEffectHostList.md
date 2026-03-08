**Example 1: 查询Windows补丁影响的主机**

查询Windows补丁影响的主机

Input: 

```
tccli cwp DescribePatchEffectHostList --cli-unfold-argument  \
    --KbId 7070 \
    --Limit 10 \
    --Offset 0 \
    --Filters.0.Name Status \
    --Filters.0.Values 0
```

Output: 
```
{
    "Response": {
        "PatchEffectHostList": [
            {
                "FirstScanTime": "2025-07-29 16:30:17",
                "FixStatus": 0,
                "HasSnapshot": 0,
                "HostVersion": 2,
                "Id": 73,
                "InstanceState": "运行中",
                "KbId": 7070,
                "LatestFixTime": "2025-07-29 16:30:17",
                "LatestScanTime": "2025-07-31 14:28:50",
                "MachineExtraInfo": {
                    "HostName": "v_llwin",
                    "InstanceID": "ins-r3qao",
                    "NetworkName": "vpc-guv4i1h5",
                    "NetworkType": 1,
                    "PrivateIP": "10.6.64.8",
                    "WanIP": "119.45.128.17"
                },
                "MachineType": "CVM",
                "Quuid": "ea71992a-b484-4d9c-882a-419fb6d0a5b0",
                "RegionId": 33,
                "RestartRequired": 0,
                "Status": 0,
                "Uuid": "ea71992a-b484-4d9c-882a-419fb6d0a5b0"
            }
        ],
        "RequestId": "475a2160-cc47-43e9-a576-ec0947badb37",
        "TotalCount": 1
    }
}
```

