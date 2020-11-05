**Example 1: Querying all real servers bound to CLB instance**



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
                        ]
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

