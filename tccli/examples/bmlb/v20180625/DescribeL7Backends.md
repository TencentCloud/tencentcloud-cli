**Example 1: 获取黑石负载均衡七层转发路径绑定的主机列表**



Input: 

```
tccli bmlb DescribeL7Backends --cli-unfold-argument  \
    --LoadBalancerId lb-47gazeml \
    --ListenerId lbl-l6fzjsx5 \
    --DomainId dm-hg8j52ud \
    --LocationId loc-02ywyc8b \
    --QueryType all
```

Output: 
```
{
    "Response": {
        "BackendSet": [
            {
                "BindType": 0,
                "Port": 99,
                "Weight": 0,
                "Status": "",
                "InstanceId": "tcpm-px13l9jh",
                "Alias": "测试机器",
                "LanIp": "10.1.100.5",
                "MgtIp": "100.73.7.9",
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
                ]
            },
            {
                "BindType": 0,
                "Port": 555,
                "Weight": 0,
                "Status": "",
                "InstanceId": "10.1.0.4",
                "Alias": "",
                "LanIp": "",
                "MgtIp": "",
                "Operates": []
            },
            {
                "BindType": 0,
                "Port": 556,
                "Weight": 0,
                "Status": "",
                "InstanceId": "10.1.0.4",
                "Alias": "",
                "LanIp": "",
                "MgtIp": "",
                "Operates": []
            }
        ],
        "RequestId": "b858eef8-8185-4eda-95f2-afd544e62ff9"
    }
}
```

