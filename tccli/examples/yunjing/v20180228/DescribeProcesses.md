**Example 1: 获取进程列表**

获取进程列表

Input: 

```
tccli yunjing DescribeProcesses --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Processes": [
            {
                "Id": 1,
                "Uuid": "6b6cd843-6bc1-4011-a74c-dc3fd26a7dd1",
                "MachineIp": "10.12.13.22",
                "MachineName": "machine-name",
                "Pid": 14456,
                "Ppid": 13456,
                "ProcessName": "mysql",
                "Username": "root",
                "Platform": "LINUX32",
                "FullPath": "/usr/local/mysql/bin/mysql",
                "CreateTime": "2018-01-01 12:12:12"
            }
        ],
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "TotalCount": 100
    }
}
```

