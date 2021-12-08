**Example 1: 搜索查询容器列表**



Input: 

```
tccli tcss DescribeAssetContainerList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "List": [
            {
                "Status": "xx",
                "ContainerName": "xx",
                "UpdateTime": "xx",
                "HostID": "xx",
                "ContainerID": "xx",
                "RamUsage": 1,
                "RunAs": "xx",
                "HostName": "xx",
                "CPUUsage": 1,
                "PublicIp": "xx",
                "ImageName": "xx",
                "HostIP": "xx",
                "Cmd": "xx",
                "ImageID": "xx",
                "POD": "xx",
                "CreateTime": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

