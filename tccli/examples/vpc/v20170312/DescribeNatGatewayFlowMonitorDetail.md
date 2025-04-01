**Example 1: 查询一个标准型NAT网关流量监控明细**

查询一个标准型NAT网关流量监控明细

Input: 

```
tccli vpc DescribeNatGatewayFlowMonitorDetail --cli-unfold-argument  \
    --TimePoint 2021-12-10T09:02:01+08:00 \
    --NatGatewayId nat-lz6rjk7n \
    --OrderField OutTraffic
```

Output: 
```
{
    "Response": {
        "NatGatewayFlowMonitorDetailSet": [
            {
                "OutTraffic": 15925824,
                "PrivateIpAddress": "2.2.2.188",
                "InPkg": 71466,
                "OutPkg": 57276,
                "InTraffic": 13526553,
                "ConcurrentConnectionCount": 999,
                "NewConnectionRate": 888
            }
        ],
        "TotalCount": 1,
        "RequestId": "d9b0cd80-3b86-4e03-8fc9-bc7de311bc73"
    }
}
```

