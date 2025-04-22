**Example 1: 获取本地提权事件列表**

获取本地提权事件列表

Input: 

```
tccli cwp DescribePrivilegeEvents --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 22,
        "List": [
            {
                "Pid": 1,
                "MachineExtraInfo": {
                    "HostName": "demo-instance",
                    "InstanceID": "ins-1002",
                    "NetworkName": "vpc-1002",
                    "NetworkType": 1,
                    "PrivateIP": "1.*.*.1",
                    "WanIP": "1.*.*.1"
                },
                "Id": 22,
                "Uuid": "cf59e3c0-b1cc-****-baac-525400ca96ee",
                "Quuid": "b9821ff5-75f0-****-b21f-13c8d36a725c",
                "Hostip": "10.*.*.125",
                "ProcessName": "nginx",
                "FullPath": "/home/ubuntu/a",
                "CmdLine": "./a ",
                "UserName": "root",
                "UserGroup": "ubuntu",
                "ProcFilePrivilege": "-rwsr-xr-x",
                "ParentProcName": "bash",
                "ParentProcUser": "ubuntu",
                "ParentProcGroup": "ubuntu",
                "ParentProcPath": "/bin/bash",
                "ProcTree": "a(root),bash(ubuntu),sshd(ubuntu),sshd(root),sshd(root),init(root)",
                "Status": 0,
                "CreateTime": "2019-08-15 15:27:52",
                "MachineName": "测试机_Linux_4"
            }
        ],
        "RequestId": "bd9aa8c8-36b6-4991-8e42-d08e80313616"
    }
}
```

