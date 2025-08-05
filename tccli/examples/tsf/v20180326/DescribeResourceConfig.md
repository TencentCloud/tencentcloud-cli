**Example 1: 获取资源配置信息**



Input: 

```
tccli tsf DescribeResourceConfig --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "5b8af5a9-bd6c-4e7b-91d4-813a41c71163",
        "Result": {
            "License": {
                "Function": [
                    {
                        "Name": "vm",
                        "Enable": true
                    },
                    {
                        "Name": "container",
                        "Enable": true
                    },
                    {
                        "Name": "mesh",
                        "Enable": true
                    },
                    {
                        "Name": "scalable",
                        "Enable": true
                    },
                    {
                        "Name": "api-governance",
                        "Enable": true
                    },
                    {
                        "Name": "gateway",
                        "Enable": true
                    },
                    {
                        "Name": "transaction",
                        "Enable": true
                    },
                    {
                        "Name": "endpoint",
                        "Enable": true
                    },
                    {
                        "Name": "template",
                        "Enable": true
                    }
                ],
                "Resource": [
                    {
                        "Name": "instance",
                        "Quota": 20
                    }
                ],
                "ExpireTime": 1583942400,
                "Countdown": 24819257
            },
            "Sts": {
                "Uin": "91000000039"
            },
            "Instance": {
                "Container": {
                    "MasterNumLimit": 0,
                    "NodeNumLimitPerSetup": 0,
                    "ImportMode": [
                        "R"
                    ]
                },
                "Vm": {
                    "ImportMode": [
                        "M",
                        "R"
                    ]
                }
            },
            "Group": {
                "Container": {
                    "AdditionalResourceRequirement": {
                        "N": {
                            "Cpu": "0.100",
                            "Mem": "125"
                        },
                        "M": {
                            "Cpu": "0.350",
                            "Mem": "375"
                        }
                    }
                }
            }
        }
    }
}
```

