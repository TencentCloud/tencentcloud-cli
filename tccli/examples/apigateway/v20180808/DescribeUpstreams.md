**Example 1: 查询vpc**



Input: 

```
tccli apigateway DescribeUpstreams --cli-unfold-argument  \
    --Limit 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Result": {
            "TotalCount": 1,
            "UpstreamSet": [
                {
                    "Retries": 1,
                    "Algorithm": "xx",
                    "UniqVpcId": "xx",
                    "Tags": [
                        {
                            "Value": "xx",
                            "Key": "xx"
                        }
                    ],
                    "UpstreamType": "xx",
                    "UpstreamHost": "xx",
                    "UpstreamId": "xx",
                    "K8sServices": [
                        {
                            "Name": "xx",
                            "Weight": 0,
                            "ClusterId": "xx",
                            "Namespace": "xx",
                            "ServiceName": "xx",
                            "ExtraLabels": [
                                {
                                    "Value": "xx",
                                    "Key": "xx"
                                }
                            ],
                            "Port": 0
                        }
                    ],
                    "UpstreamName": "xx",
                    "HealthChecker": {
                        "UnhealthyTimeout": 1,
                        "ActiveCheckInterval": 1,
                        "ActiveRequestHeader": [
                            {}
                        ],
                        "TimeoutThreshold": 1,
                        "HealthyHttpStatus": "xx",
                        "TcpFailureThreshold": 1,
                        "EnableActiveCheck": true,
                        "UnhealthyHttpStatus": "xx",
                        "ActiveCheckHttpPath": "xx",
                        "EnablePassiveCheck": true,
                        "HttpFailureThreshold": 1,
                        "ActiveCheckTimeout": 1
                    },
                    "CreatedTime": "2020-09-22T00:00:00+00:00",
                    "Nodes": [
                        {
                            "Weight": 1,
                            "Tags": [
                                "xx"
                            ],
                            "Healthy": "xx",
                            "ClusterId": "xx",
                            "NameSpace": "xx",
                            "Source": "xx",
                            "VmInstanceId": "xx",
                            "Host": "xx",
                            "ServiceName": "xx",
                            "UniqueServiceName": "xx",
                            "Port": 1
                        }
                    ],
                    "Scheme": "xx",
                    "UpstreamDescription": "xx"
                }
            ]
        },
        "RequestId": "xx"
    }
}
```

