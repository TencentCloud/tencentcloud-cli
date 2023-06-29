**Example 1: 查询端口占用列表**

查询端口占用列表

Input: 

```
tccli tcss DescribeAssetPortList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Type": "abc",
                "PublicIP": "abc",
                "PublicPort": 1,
                "ContainerPort": 1,
                "ContainerPID": 1,
                "ContainerName": "abc",
                "HostID": "abc",
                "HostIP": "abc",
                "ProcessName": "abc",
                "ListenContainer": "abc",
                "ListenHost": "abc",
                "RunAs": "abc",
                "HostName": "abc",
                "PublicIp": "abc",
                "NodeID": "abc",
                "PodIP": "abc",
                "PodName": "abc",
                "NodeType": "abc",
                "NodeUniqueID": "abc"
            }
        ],
        "TotalCount": 1,
        "RequestId": "abc"
    }
}
```

