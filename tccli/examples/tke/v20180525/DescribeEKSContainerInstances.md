**Example 1: 查询容器实例**



Input: 

```
tccli tke DescribeEKSContainerInstances --cli-unfold-argument  \
    --EksCiIds eksci-6mr3o7eu
```

Output: 
```
{
    "Response": {
        "RequestId": "34d9ea5a-6e9e-4384-88da-84229e133412",
        "TotalCount": 1,
        "EksCis": [
            {
                "EksCiId": "eksci-iu09upos",
                "EksCiName": "未命名",
                "Memory": 2,
                "Cpu": 1,
                "SecurityGroupIds": [
                    "sg-12345678"
                ],
                "RestartPolicy": "Always",
                "VpcId": "vpc-12345678",
                "SubnetId": "subnet-12345678",
                "Status": "Running",
                "CreationTime": "2021-06-24 03:32:02 +0000 UTC",
                "SucceededTime": "2021-06-24 11:32:21 +0000 UTC",
                "Containers": [
                    {
                        "Image": "ccr.ccs.tencentyun.com/ploto/cputest:1.4",
                        "Name": "simple-cputest",
                        "Cpu": 0,
                        "Memory": 0,
                        "Commands": [
                            "sleep"
                        ],
                        "Args": [
                            "100000"
                        ],
                        "EnvironmentVars": [],
                        "CurrentState": {
                            "StartTime": "2021-06-24 03:32:43.420750215 +0000 UTC",
                            "State": "running",
                            "FinishTime": "0001-01-01 00:00:00 +0000 UTC",
                            "ExitCode": 0,
                            "Reason": "",
                            "Message": "",
                            "RestartCount": 0
                        },
                        "RestartCount": 0,
                        "WorkingDir": ""
                    }
                ],
                "InitContainers": null,
                "EksCiVolume": {
                    "CbsVolumes": null,
                    "NfsVolumes": null
                },
                "SecurityContext": null,
                "PrivateIp": "10.1.0.1",
                "EipAddress": "",
                "CpuType": "amd,intel",
                "GpuType": "",
                "GpuCount": 0,
                "CamRoleName": ""
            }
        ]
    }
}
```

