**Example 1: 查询db服务列表**



Input: 

```
tccli tcss DescribeAssetDBServiceList --cli-unfold-argument ```

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
                    "tcp://:::3306"
                ]
            },
            {
                "ContainerName": "xx",
                "Type": "xx",
                "HostID": "xx",
                "ContainerId": "xx",
                "Exe": "xx",
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
                "Version": "xx",
                "ServiceID": "xx",
                "HostIP": "xx",
                "Pids": [
                    1
                ],
                "Parameter": "xx",
                "Listen": [
                    "tcp://:::6379",
                    "tcp://0.0.0.0:6379"
                ]
            }
        ],
        "RequestId": "xx"
    }
}
```

