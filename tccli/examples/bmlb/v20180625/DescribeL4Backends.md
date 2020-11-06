**Example 1: 获取黑石负载均衡四层监听器绑定的主机列表**



Input: 

```
tccli bmlb DescribeL4Backends --cli-unfold-argument  \
    --LoadBalancerId lb-dyxceyv5 \
    --ListenerId lbl-i4go349z
```

Output: 
```
{
    "Response": {
        "BackendSet": [
            {
                "BindType": 0,
                "Port": 5000,
                "Weight": 100,
                "Status": "Dead",
                "InstanceId": "cpm-bujx6q9x",
                "Alias": "测试机器",
                "LanIp": "10.10.1.3",
                "Operates": [
                    "modifyDeviceAlias",
                    "renewDevice",
                    "shutdownDevice",
                    "rebootDevice",
                    "reloadDeviceOs",
                    "resetPasswd",
                    "bindEip",
                    "unbindEip",
                    "isolateDevice",
                    "bindLb",
                    "unbindLb",
                    "offlineDevice",
                    "runUserCmd",
                    "changeLanIp",
                    "CreateCustomImage",
                    "bareMetalMigration"
                ],
                "ProbePort": -1
            }
        ],
        "RequestId": "d401377c-ac68-48ad-ac06-f7d0ca4e4ff6"
    }
}
```

