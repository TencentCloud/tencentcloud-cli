**Example 1: 查询app服务列表**



Input: 

```
tccli tcss DescribeAssetAppServiceList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "List": [
            {
                "ContainerName": "xx",
                "Parameter": "xx",
                "HostID": "xx",
                "Version": "xx",
                "ContainerId": "xx",
                "AccessLog": "xx",
                "Config": "xx",
                "RunAs": "xx",
                "HostName": "xx",
                "ErrorLog": "xx",
                "DataPath": "xx",
                "MainType": "xx",
                "PublicIp": "xx",
                "WebRoot": "xx",
                "ProcessCnt": 1,
                "Exe": "xx",
                "ServiceID": "xx",
                "HostIP": "xx",
                "Pids": [
                    1
                ],
                "Type": "xx",
                "Listen": [
                    "tcp://:::10054"
                ]
            }
        ],
        "RequestId": "xx"
    }
}
```

