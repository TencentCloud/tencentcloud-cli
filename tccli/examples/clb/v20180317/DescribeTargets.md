**Example 1: 通过Location过滤查询后端服务列表**

当负载均衡的7层监听器规则太多，而只想查询某个规则下的服务列表时，可通过Filters过滤location-id。

Input: 

```
tccli clb DescribeTargets --cli-unfold-argument  \
    --LoadBalancerId lb-12345678 \
    --Filters.0.Name location-id \
    --Filters.0.Values loc-12345678
```

Output: 
```
{
    "Response": {
        "Listeners": [
            {
                "ListenerId": "lbl-12345678",
                "Protocol": "HTTP",
                "Port": 80,
                "Rules": [
                    {
                        "LocationId": "loc-12345678",
                        "Domain": "123.com",
                        "Url": "/",
                        "Targets": [
                            {
                                "Type": "CVM",
                                "InstanceId": "ins-12345678",
                                "Port": 80,
                                "Weight": 10,
                                "PublicIpAddresses": null,
                                "PrivateIpAddresses": [
                                    "172.16.0.100"
                                ],
                                "InstanceName": "123",
                                "RegisteredTime": "2023-01-01",
                                "EniId": "eni-12345678"
                            }
                        ],
                        "FunctionTargets": null
                    }
                ],
                "Targets": null,
                "EndPort": 0
            }
        ],
        "RequestId": "038afb75-7303-48da-abdc-e25f0cbfda0f"
    }
}
```

**Example 2: 查询负载均衡实例上绑定的所有后端服务**

查询负载均衡实例上绑定的所有后端服务

Input: 

```
tccli clb DescribeTargets --cli-unfold-argument  \
    --LoadBalancerId lb-10iq9lou
```

Output: 
```
{
    "Response": {
        "Listeners": [
            {
                "ListenerId": "lbl-4fo6k8na",
                "Protocol": "HTTP",
                "Port": 80,
                "Rules": [
                    {
                        "LocationId": "loc-o9732aw0",
                        "Domain": "www.123.com",
                        "Url": "/",
                        "Targets": [
                            {
                                "Type": "cvm",
                                "PrivateIpAddresses": [
                                    "172.16.0.12"
                                ],
                                "EniId": "",
                                "PublicIpAddresses": null,
                                "InstanceName": "abcd1234",
                                "Port": 555,
                                "Weight": 10,
                                "InstanceId": "ins-19425y2y",
                                "RegisteredTime": "2019-07-12 16:22:02"
                            }
                        ],
                        "FunctionTargets": []
                    }
                ],
                "Targets": null
            },
            {
                "ListenerId": "lbl-4ue2rpl2",
                "Protocol": "TCP",
                "Port": 888,
                "Rules": null,
                "Targets": [
                    {
                        "Type": "cvm",
                        "PrivateIpAddresses": [
                            "172.16.0.12"
                        ],
                        "EniId": "",
                        "PublicIpAddresses": null,
                        "InstanceName": "abcd1234",
                        "Port": 666,
                        "Weight": 40,
                        "InstanceId": "ins-19425y2y",
                        "RegisteredTime": "2019-07-12 16:22:54"
                    }
                ]
            }
        ],
        "RequestId": "a5cbe92d-c7f2-41d4-8343-3cb42c3fd1dd"
    }
}
```

