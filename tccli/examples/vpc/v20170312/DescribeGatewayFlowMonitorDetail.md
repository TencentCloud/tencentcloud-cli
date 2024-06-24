**Example 1: 查询一个传统型NAT网关流量监控明细**

查询一个传统型NAT网关流量监控明细

Input: 

```
tccli vpc DescribeGatewayFlowMonitorDetail --cli-unfold-argument  \
    --TimePoint '2019-02-28 18:15:20' \
    --NatId nat-lz6rjk7n \
    --OrderField OutTraffic \
    --OrderDirection DESC
```

Output: 
```
{
    "Response": {
        "GatewayFlowMonitorDetailSet": [
            {
                "PrivateIpAddress": "172.20.65.74",
                "InPkg": 182,
                "OutPkg": 263,
                "InTraffic": 17316,
                "OutTraffic": 35269,
                "NewConnectionRate": 0,
                "ConcurrentConnectionCount": 0
            },
            {
                "PrivateIpAddress": "172.20.65.63",
                "InPkg": 0,
                "OutPkg": 20,
                "InTraffic": 0,
                "OutTraffic": 1960,
                "NewConnectionRate": 0,
                "ConcurrentConnectionCount": 0
            },
            {
                "PrivateIpAddress": "172.20.65.70",
                "InPkg": 0,
                "OutPkg": 20,
                "InTraffic": 0,
                "OutTraffic": 1960,
                "NewConnectionRate": 0,
                "ConcurrentConnectionCount": 0
            },
            {
                "PrivateIpAddress": "172.20.65.172",
                "InPkg": 0,
                "OutPkg": 20,
                "InTraffic": 0,
                "OutTraffic": 1960,
                "NewConnectionRate": 0,
                "ConcurrentConnectionCount": 0
            },
            {
                "PrivateIpAddress": "172.20.65.249",
                "InPkg": 0,
                "OutPkg": 20,
                "InTraffic": 0,
                "OutTraffic": 1960,
                "NewConnectionRate": 0,
                "ConcurrentConnectionCount": 0
            }
        ],
        "TotalCount": 261,
        "RequestId": "0fc9884d-7aa1-4d95-95d3-7945108d2b10"
    }
}
```

**Example 2: 查询一个标准型NAT网关流量监控明细**

查询一个标准型NAT网关流量监控明细

Input: 

```
tccli vpc DescribeGatewayFlowMonitorDetail --cli-unfold-argument  \
    --TimePoint '2024-06-24 14:03:00' \
    --NatId nat-g0pwqefo \
    --OrderField InTraffic \
    --OrderDirection DESC
```

Output: 
```
{
    "Response": {
        "GatewayFlowMonitorDetailSet": [
            {
                "PrivateIpAddress": "2.2.2.2",
                "InPkg": 5455,
                "OutPkg": 4444,
                "InTraffic": 1048576,
                "OutTraffic": 1234567,
                "NewConnectionRate": 8888,
                "ConcurrentConnectionCount": 9999
            }
        ],
        "TotalCount": 1,
        "RequestId": "396e6170-f2ce-4233-9405-9a2e5ce8b0b5"
    }
}
```

