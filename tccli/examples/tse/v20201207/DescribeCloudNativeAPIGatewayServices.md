**Example 1: 查询云原生网关服务列表**

查询云原生网关服务列表


Input: 

```
tccli tse DescribeCloudNativeAPIGatewayServices --cli-unfold-argument  \
    --GatewayId abc \
    --Limit 0 \
    --Offset 0 \
    --Filters.0.Key abc \
    --Filters.0.Value abc
```

Output: 
```
{
    "Response": {
        "Result": {
            "ServiceList": [
                {
                    "Name": "abc",
                    "ID": "abc",
                    "Tags": [
                        "abc"
                    ],
                    "UpstreamInfo": {
                        "Host": "abc",
                        "Port": 0,
                        "SourceID": "abc",
                        "Namespace": "abc",
                        "ServiceName": "abc",
                        "Targets": [
                            {
                                "Host": "abc",
                                "Port": 0,
                                "Weight": 0,
                                "Health": "abc",
                                "CreatedTime": "abc",
                                "Source": "abc"
                            }
                        ],
                        "SourceType": "abc",
                        "ScfType": "abc",
                        "ScfNamespace": "abc",
                        "ScfLambdaName": "abc",
                        "ScfLambdaQualifier": "abc",
                        "SlowStart": 0,
                        "Algorithm": "abc",
                        "AutoScalingGroupID": "abc",
                        "AutoScalingCvmPort": 1,
                        "AutoScalingTatCmdStatus": "abc",
                        "AutoScalingHookStatus": "abc",
                        "SourceName": "abc",
                        "RealSourceType": "abc"
                    },
                    "UpstreamType": "abc",
                    "CreatedTime": "abc",
                    "Editable": true
                }
            ],
            "TotalCount": 0
        },
        "RequestId": "abc"
    }
}
```

