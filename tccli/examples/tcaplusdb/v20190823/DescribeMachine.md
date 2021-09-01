**Example 1: 查询独占集群机器资源**

查询独占集群可用机器资源

Input: 

```
tccli tcaplusdb DescribeMachine --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "PoolList": [
            {
                "PoolUid": 1,
                "Ipv6Enable": 0,
                "AvailableAppCount": 100,
                "ServerList": [
                    {
                        "ServerUid": "svr1",
                        "MachineType": "T1"
                    },
                    {
                        "ServerUid": "svr2",
                        "MachineType": "T2"
                    }
                ],
                "ProxyList": [
                    {
                        "ProxyUid": "proxy1",
                        "MachineType": "T1"
                    },
                    {
                        "ProxyUid": "proxy1",
                        "MachineType": "T2"
                    }
                ]
            },
            {
                "PoolUid": 2,
                "Ipv6Enable": 0,
                "AvailableAppCount": 100,
                "ServerList": [
                    {
                        "ServerUid": "svr1",
                        "MachineType": "T1"
                    },
                    {
                        "ServerUid": "svr2",
                        "MachineType": "T2"
                    }
                ],
                "ProxyList": [
                    {
                        "ProxyUid": "proxy1",
                        "MachineType": "T1"
                    },
                    {
                        "ProxyUid": "proxy1",
                        "MachineType": "T2"
                    }
                ]
            }
        ],
        "RequestId": "34680b61-9836-44d9-bae9-e231f4b61a48"
    }
}
```

