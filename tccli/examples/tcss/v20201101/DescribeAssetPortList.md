**Example 1: 查询端口占用列表**



Input: 

```
tccli tcss DescribeAssetPortList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "List": [
            {
                "ContainerName": "xx",
                "HostID": "xx",
                "Type": "xx",
                "RunAs": "xx",
                "HostName": "xx",
                "ContainerPID": 1,
                "ListenContainer": "xx",
                "PublicIP": "xx",
                "ProcessName": "xx",
                "HostIP": "xx",
                "PublicIp": "xx",
                "PublicPort": 1,
                "ContainerPort": 1,
                "ListenHost": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

