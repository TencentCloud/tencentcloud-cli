**Example 1: 获取进程列表**

获取进程列表

Input: 

```
tccli cwp DescribeProcesses --cli-unfold-argument  \
    --Uuid xxx \
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
                "Uuid": "xxx",
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

