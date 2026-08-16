**Example 1: 查询所有集群**



Input: 

```
tccli mna GetCustomerGatewayClusterList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "ClusterList": [
            {
                "ClusterId": "cluster-vpqultrhw6",
                "ClusterName": "jacky-test-cluster",
                "CreateTime": 1785132647,
                "GatewayList": [
                    {
                        "CreateTime": 1785144,
                        "GatewayId": "mpgw-s6mubb4u11",
                        "GatewayIp": "21.0.***.246",
                        "GatewayName": "multipath-bj-test1-0",
                        "InstanceSize": 4,
                        "RegisterCenterUrl": "reg-*********.multipath.tencent-cloud.com:9300",
                        "Status": 1,
                        "TelemetryUrl": "21.0.21.***:65002",
                        "Token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJTdGFuZGFyZENsYWltcyI6eyJpYX******ODUxNDQxODAuOTU1MjE3LCJuYmYiOjE3ODUxNDQxODAuOTU1MjE3OH0sImd3SWQiOiJtcGd3LXM2bXViYjR1MTEiLCJtZ210SXAiOiIyMS4wLjE3My4yNDYifQ.fvqaWPrJReE6p4S73tdcs1YFJ2UIc-U6YidE-yk6V-4",
                        "Username": "jacky"
                    }
                ],
                "InstanceCount": 1,
                "PublicIp": "39.156.***.229:443"
            }
        ],
        "TotalCount": 1,
        "RequestId": "31159f39-3adc-45cb-87ab-d946abe27067"
    }
}
```

