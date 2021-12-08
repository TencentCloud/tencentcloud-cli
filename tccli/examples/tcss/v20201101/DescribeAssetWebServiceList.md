**Example 1: 查询web服务列表**



Input: 

```
tccli tcss DescribeAssetWebServiceList --cli-unfold-argument ```

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
                    1,
                    1,
                    1,
                    1,
                    1,
                    1
                ],
                "Type": "xx",
                "Listen": [
                    "tcp://0.0.0.0:80"
                ]
            }
        ],
        "RequestId": "xx"
    }
}
```

