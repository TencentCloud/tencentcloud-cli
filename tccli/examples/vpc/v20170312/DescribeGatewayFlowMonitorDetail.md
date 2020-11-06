**Example 1: Querying the traffic monitoring details of a NAT gateway**



Input: 

```
tccli vpc DescribeGatewayFlowMonitorDetail --cli-unfold-argument  \
    --TimePoint '2019-02-28 18:15:20' \
    --NatId nat-lz6rjk7n \
    --Limit 5 \
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
                "OutTraffic": 35269
            },
            {
                "PrivateIpAddress": "172.20.65.63",
                "InPkg": 0,
                "OutPkg": 20,
                "InTraffic": 0,
                "OutTraffic": 1960
            },
            {
                "PrivateIpAddress": "172.20.65.70",
                "InPkg": 0,
                "OutPkg": 20,
                "InTraffic": 0,
                "OutTraffic": 1960
            },
            {
                "PrivateIpAddress": "172.20.65.172",
                "InPkg": 0,
                "OutPkg": 20,
                "InTraffic": 0,
                "OutTraffic": 1960
            },
            {
                "PrivateIpAddress": "172.20.65.249",
                "InPkg": 0,
                "OutPkg": 20,
                "InTraffic": 0,
                "OutTraffic": 1960
            }
        ],
        "TotalCount": 261,
        "RequestId": "0fc9884d-7aa1-4d95-95d3-7945108d2b10"
    }
}
```

