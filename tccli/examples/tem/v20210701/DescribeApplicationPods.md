**Example 1: 获取应用实例列表**

获取应用实例列表

Input: 

```
tccli tem DescribeApplicationPods --cli-unfold-argument  \
    --Status xx \
    --EnvironmentId xx \
    --Offset 0 \
    --SourceChannel 0 \
    --Limit 0 \
    --PodName xx \
    --ApplicationId xx
```

Output: 
```
{
    "Response": {
        "Result": {
            "TotalCount": 0,
            "Limit": 0,
            "RequestId": "xx",
            "PodList": [
                {
                    "Webshell": "xx",
                    "Status": "xx",
                    "RestartCount": 0,
                    "StartTime": "xx",
                    "Zone": "xx",
                    "PodId": "xx",
                    "NodeInfo": {
                        "SubnetId": "xx",
                        "Cidr": "xx",
                        "AvailableIpCount": "xx",
                        "Name": "xx",
                        "Zone": "xx"
                    },
                    "VersionId": "xx",
                    "UnhealthyWarningMsg": "xx",
                    "DeployVersion": "xx",
                    "PodIp": "xx",
                    "ContainerState": "xx",
                    "Ready": true,
                    "ApplicationName": "xx",
                    "CreateTime": "xx",
                    "Unhealthy": true
                }
            ],
            "Offset": 0
        },
        "RequestId": "xx"
    }
}
```

