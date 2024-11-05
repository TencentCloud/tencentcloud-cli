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
                "NodeID": "mix-GOmf****",
                "NodeType": "NORMAL",
                "NodeUniqueID": "896e349d-2e7d-4151-a26f-4e9fdafe****",
                "PID": 834,
                "PodIP": "10.0.1.92",
                "PodName": "agent-test-2zrp7",
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

