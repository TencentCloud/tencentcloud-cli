**Example 1: 查询进程列表**

查询进程列表

Input: 

```
tccli tcss DescribeAssetProcessList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "CmdLine": "/bin/bash",
                "ContainerName": "/srv_test",
                "ContainerPID": 1,
                "Exe": "/usr/bin/bash",
                "HostID": "8bc803fd-d85d-47b8-9e2b-9644674be677",
                "HostIP": "1.1.1.1",
                "HostName": "机器名称",
                "NodeID": "",
                "NodeType": "NORMAL",
                "NodeUniqueID": "",
                "PID": 834,
                "PodIP": "",
                "PodName": "",
                "ProcessName": "bash",
                "PublicIp": "1.1.1.1",
                "RunAs": "root:root",
                "StartTime": "2024-10-17 15:00:47 +0000 UTC"
            }
        ],
        "TotalCount": 1,
        "RequestId": "8bc803fd-d85d-47b8-9e2b-9644674be677"
    }
}
```

