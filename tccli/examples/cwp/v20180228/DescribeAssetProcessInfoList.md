**Example 1: 获取资产管理进程列表**



Input: 

```
tccli cwp DescribeAssetProcessInfoList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Total": 1,
        "Process": [
            {
                "MachineIp": "10.0.0.11",
                "MachineWanIp": "110.84.0.11",
                "Quuid": "acdd5474-6360-4fd4-bfc7-843162cb8116",
                "Uuid": "acdd5474-6360-4fd4-bfc7-843162cb8116",
                "OsInfo": "CentOs Bit64",
                "ProjectId": 1,
                "Tag": [
                    {
                        "Rid": 0,
                        "Name": "test-name",
                        "TagId": 1
                    }
                ],
                "Name": "test-name",
                "Desc": "none",
                "Path": "/root",
                "Pid": "10011",
                "User": "root",
                "StartTime": "2024-10-11 12:23:34",
                "Param": "iparam",
                "Tty": "/bin",
                "Version": "0.1.1.1",
                "GroupName": "test-name",
                "Md5": "708cae4cf814c3deda4208da228fad4e",
                "Ppid": "22",
                "ParentProcessName": "test-name",
                "Status": "Running",
                "HasSign": 1,
                "InstallByPackage": 1,
                "PackageName": "test-name",
                "MachineName": "test-name",
                "UpdateTime": "2024-10-11 12:23:34",
                "FirstTime": "2024-10-11 12:23:34",
                "IsNew": 0,
                "MachineExtraInfo": {
                    "WanIP": "110.84.0.11",
                    "PrivateIP": "10.0.0.11",
                    "NetworkType": 0,
                    "NetworkName": "vpc-11",
                    "InstanceID": "ins-aj28fjz",
                    "HostName": "test-name"
                }
            }
        ],
        "RequestId": "37b6df34-68f1-4ab8-a3d8-7b89de604c82"
    }
}
```

