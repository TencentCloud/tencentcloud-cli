**Example 1: 示例**



Input: 

```
tccli mqtt DescribeClusterAdminForOperation --cli-unfold-argument  \
    --ClusterId mqtt-broker-cddev-3
```

Output: 
```
{
    "Response": {
        "AccessKey": "***",
        "ClusterId": "mqtt-broker-cddev-3",
        "ClusterStatus": "RUNNING",
        "ClusterVersion": "1",
        "CreateTime": 1777453726000,
        "DeployEnv": "LEGACY",
        "NameServer": "mock.nameserver-3.loca:9876",
        "Room": "mqtt-namesrv-cddev-3",
        "SecretKey": "****",
        "UpdateTime": 1777454515000,
        "RequestId": "92f2cc1a-4fef-4955-9e68-5d7a8fff2a2e"
    }
}
```

