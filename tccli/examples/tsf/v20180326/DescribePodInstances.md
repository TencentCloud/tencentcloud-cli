**Example 1: DescribePodInstances**



Input: 

```
tccli tsf DescribePodInstances --cli-unfold-argument  \
    --GroupId group-6a73w4v5\
    --Offset 0\
    --Limit 20
```

Output: 
```
{
    "Response": {
        "RequestId": "4c78ccfd-c990-4182-bc53-2a9f417696cf",
        "Result": {
            "TotalCount": 1,
            "Content": [
                {
                    "Reason": "",
                    "RestartCount": 0,
                    "Ip": "172.18.1.27",
                    "NodeIp": "10.2.12.141",
                    "Runtime": "7d 20h",
                    "InstanceStatus": null,
                    "Containers ": [
                        {
                            "Name": "group-6a73w4v5-agent-docker",
                            "ContainerId": "docker://fe4265940b1be1be1d11c7eae55dc61263798c449a610ecb3602be56787831a9",
                            "Status": "Running",
                            "Reason": "",
                            "Image": "ccr.ccs.tencentyun.com/tsf_base/agent:1.12"
                        },
                        {
                            "Name": "group-6a73w4v5-docker",
                            "ContainerId": "docker://e9e09f700be21da3180c6e827defe1fc7189d29ab26ec7bc3a4f9f38080f1ae3",
                            "Status": "Running",
                            "Reason": "",
                            "Image": "ccr.ccs.tencentyun.com/tsf_100006174298/prod_pay_center:v19-3-12"
                        }
                    ],
                    "CreatedAt": "2019-05-21 20:46:06",
                    "InstanceAvailableStatus": null,
                    "ServiceInstanceStatus": "Running",
                    "ReadyCount": 2,
                    "PodName": "prod-pay-center-a-2345103634-4x151",
                    "PodId": "6646495c-7bc6-11e9-b713-86e5a1f74de4",
                    "Status": "Running"
                }
            ]
        }
    }
}
```

