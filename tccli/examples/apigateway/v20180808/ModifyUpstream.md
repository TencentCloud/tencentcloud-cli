**Example 1: 修改vpc通道信息**

修改vpc通道信息

Input: 

```
tccli apigateway ModifyUpstream --cli-unfold-argument  \
    --UpstreamId upstream-0c96l2bo \
    --Retries 4 \
    --UpstreamName test \
    --UpstreamHost www.a.com \
    --UpstreamDescription test
```

Output: 
```
{
    "Response": {
        "Result": {
            "UpstreamId": "abc",
            "UpstreamName": "abc",
            "UpstreamDescription": "abc",
            "Scheme": "abc",
            "Algorithm": "abc",
            "UniqVpcId": "abc",
            "Retries": 1,
            "Nodes": [
                {
                    "VmInstanceId": "abc",
                    "Host": "abc",
                    "Port": 1,
                    "Weight": 1,
                    "Tags": [
                        "abc"
                    ],
                    "Healthy": "abc",
                    "ServiceName": "abc",
                    "NameSpace": "abc",
                    "ClusterId": "abc",
                    "Source": "abc",
                    "UniqueServiceName": "abc"
                }
            ],
            "CreatedTime": "2020-09-22T00:00:00+00:00",
            "HealthChecker": {
                "EnableActiveCheck": true,
                "EnablePassiveCheck": true,
                "ActiveCheckHttpPath": "abc",
                "ActiveCheckTimeout": 1,
                "ActiveCheckInterval": 1,
                "ActiveRequestHeader": [
                    {}
                ],
                "UnhealthyTimeout": 1,
                "HealthyHttpStatus": "abc",
                "UnhealthyHttpStatus": "abc",
                "TcpFailureThreshold": 1,
                "TimeoutThreshold": 1,
                "HttpFailureThreshold": 1
            },
            "UpstreamType": "abc",
            "K8sServices": [
                {
                    "Name": "abc",
                    "Weight": 0,
                    "ClusterId": "abc",
                    "Namespace": "abc",
                    "ServiceName": "abc",
                    "Port": 0,
                    "ExtraLabels": [
                        {
                            "Key": "abc",
                            "Value": "abc"
                        }
                    ]
                }
            ],
            "UpstreamHost": "abc"
        },
        "RequestId": "abc"
    }
}
```

