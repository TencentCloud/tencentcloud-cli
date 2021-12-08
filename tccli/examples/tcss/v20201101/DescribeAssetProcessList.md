**Example 1: 查询进程列表**

查询进程列表

Input: 

```
tccli tcss DescribeAssetProcessList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "List": [
            {
                "ContainerName": "xx",
                "Exe": "xx",
                "ProcessName": "xx",
                "PID": 1,
                "RunAs": "xx",
                "HostName": "xx",
                "ContainerPID": 1,
                "PublicIp": "xx",
                "CmdLine": "xx",
                "HostID": "xx",
                "StartTime": "xx",
                "HostIP": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

