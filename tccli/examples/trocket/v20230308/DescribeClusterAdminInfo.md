**Example 1: 标准请求**

标准请求

Input: 

```
tccli trocket DescribeClusterAdminInfo --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "ClusterAdminInfos": [
            {
                "AccessKey": "ZlbUZYqqsvYaxlrZ",
                "ClusterId": "rmqbroker-cd-jazjroda",
                "ClusterStatus": "RUNNING",
                "ClusterVersion": "5.0",
                "DeployEnv": "LEGACY",
                "Room": "1",
                "SecretKey": "ZlbUZYqqsvYaxlrZ"
            },
            {
                "AccessKey": "ZlbUZYqqsvYaxlrZ",
                "ClusterId": "rmqbroker-cd-wdx43rwg",
                "ClusterStatus": "RUNNING",
                "ClusterVersion": "5.0",
                "DeployEnv": "LEGACY",
                "Room": "1",
                "SecretKey": "ZlbUZYqqsvYaxlrZ"
            },
            {
                "AccessKey": "ZlbUZYqqsvYaxlrZ",
                "ClusterId": "rmq5-room-cd-1",
                "ClusterStatus": "RUNNING",
                "ClusterVersion": "5.0",
                "DeployEnv": "LEGACY",
                "Room": "1",
                "SecretKey": "ZlbUZYqqsvYaxlrZ"
            },
            {
                "AccessKey": "ZlbUZYqqsvYaxlrZ",
                "ClusterId": "rmqbroker-cd-room1",
                "ClusterStatus": "RUNNING",
                "ClusterVersion": "5.0",
                "DeployEnv": "LEGACY",
                "Room": "1",
                "SecretKey": "ZlbUZYqqsvYaxlrZ"
            },
            {
                "AccessKey": "ZlbUZYqqsvYaxlrZ",
                "ClusterId": "rocketmq-stable",
                "ClusterStatus": "RUNNING",
                "ClusterVersion": "4.9.3",
                "DeployEnv": "LEGACY",
                "Room": "1",
                "SecretKey": "ZlbUZYqqsvYaxlrZ"
            }
        ],
        "RequestId": "df71123b-cf52-4ccd-b667-439159f22566",
        "TotalCount": 5
    }
}
```

