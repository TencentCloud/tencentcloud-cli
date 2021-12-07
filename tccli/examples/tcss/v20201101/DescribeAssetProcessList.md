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
                "StartTime": "2021-01-14T02:25:29Z",
                "RunAs": "work:work",
                "CmdLine": "sh",
                "Exe": "/bin/busybox",
                "PID": 3766,
                "ContainerPID": 1,
                "ContainerName": "/practical_sanderson",
                "HostID": "5cd1c13e-d18a-4904-ada3-a2efed76c6f9",
                "HostIP": "10.0.0.13",
                "ProcessName": "busybox"
            }
        ],
        "RequestId": "b62e7e38-ecb9-4014-a8ba-5ebf39c1488f",
        "TotalCount": 87
    }
}
```

