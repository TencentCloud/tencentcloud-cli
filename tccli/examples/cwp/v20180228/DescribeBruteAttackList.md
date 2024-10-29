**Example 1: 获取密码破解列表**

获取密码破解列表

Input: 

```
tccli cwp DescribeBruteAttackList --cli-unfold-argument  \
    --Limit 1 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "BruteAttackList": [
            {
                "Id": 202443000000,
                "Uuid": "05f0bcab-726c-4ea4-8109-bcd03d5598f7",
                "MachineIp": "172.16.0.40",
                "MachineName": "机器名称",
                "UserName": "root",
                "SrcIp": "1.1.1.1",
                "Status": "SUCCESS",
                "EventType": 300,
                "Country": 1,
                "City": 343,
                "Province": 32,
                "CreateTime": "2024-10-22 19:50:12",
                "ModifyTime": "2024-10-22 20:06:34",
                "BanStatus": 1,
                "Count": 436,
                "Quuid": "05f0bcab-726c-4ea4-8109-bcd03d5598f7",
                "IsProVersion": true,
                "Protocol": "ssh",
                "Port": 22,
                "InstanceId": "ins-12332112",
                "Location": "中国香港::",
                "DataStatus": 0,
                "RiskLevel": 2,
                "MachineExtraInfo": {
                    "WanIP": "1.1.1.1",
                    "PrivateIP": "",
                    "NetworkType": 0,
                    "NetworkName": "",
                    "InstanceID": "ins-12332112",
                    "HostName": ""
                },
                "DataFrom": 0,
                "AttackStatusDesc": "破解成功",
                "BanExpiredTime": ""
            }
        ],
        "RequestId": "be6f6eec-0825-4e67-ab9a-c8568bbf736c"
    }
}
```

