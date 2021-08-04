**Example 1: 查询小租户网关信息**



Input: 

```
tccli tcb DescribeStandaloneGateway --cli-unfold-argument  \
    --EnvId env-test-xxx
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "StandaloneGatewayList": [
            {
                "GatewayName": "x-tcb-reserved-gw-envoy-demo",
                "CPU": 0.25,
                "Mem": 1,
                "PackageVersion": "starter",
                "GatewayAlias": "StandaloneGateway",
                "VpcId": "vpc-73afxxfa",
                "SubnetIds": [
                    "subnet-9xnlrqj5"
                ],
                "GatewayDesc": "gateway",
                "GateWayStatus": "success",
                "ServiceInfo": {
                    "ServiceName": "gateway",
                    "Status": "off"
                }
            }
        ],
        "RequestId": "51a33e48-a808-4fe7-8c02-4e7be5245351"
    }
}
```

