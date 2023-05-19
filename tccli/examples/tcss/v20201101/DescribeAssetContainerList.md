**Example 1: 搜索查询容器列表**

搜索查询容器列表

Input: 

```
tccli tcss DescribeAssetContainerList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "ContainerID": "abc",
                "ContainerName": "abc",
                "Status": "abc",
                "CreateTime": "abc",
                "RunAs": "abc",
                "Cmd": "abc",
                "CPUUsage": 1,
                "RamUsage": 1,
                "ImageName": "abc",
                "ImageID": "abc",
                "POD": "abc",
                "HostID": "abc",
                "HostIP": "abc",
                "UpdateTime": "abc",
                "HostName": "abc",
                "PublicIp": "abc",
                "NetStatus": "abc",
                "NetSubStatus": "abc",
                "IsolateSource": "abc",
                "IsolateTime": "abc",
                "PodName": "abc"
            }
        ],
        "TotalCount": 1,
        "RequestId": "abc"
    }
}
```

