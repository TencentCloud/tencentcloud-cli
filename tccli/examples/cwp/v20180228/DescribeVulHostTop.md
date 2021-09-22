**Example 1: 获取服务器风险top列表**

获取服务器风险top列表

Input: 

```
tccli cwp DescribeVulHostTop --cli-unfold-argument  \
    --Top 5
```

Output: 
```
{
    "Response": {
        "RequestId": "f14ce73f-50d7-4c36-af1d-fc33dae510c4",
        "VulHostTopList": [
            {
                "HostName": "v_lwjlin_centos_林",
                "Quuid": "979c93e9-fad9-4a6f-8c7e-325a5b30ac7b",
                "VulLevelList": [
                    {
                        "VulLevel": 2,
                        "VulCount": 616
                    },
                    {
                        "VulLevel": 1,
                        "VulCount": 209
                    },
                    {
                        "VulLevel": 3,
                        "VulCount": 363
                    }
                ],
                "Score": 1188
            },
            {
                "HostName": "漏洞告警临时测试",
                "Quuid": "0d751f60-b0a9-4189-a705-010493a99d8b",
                "VulLevelList": [
                    {
                        "VulLevel": 2,
                        "VulCount": 208
                    },
                    {
                        "VulLevel": 1,
                        "VulCount": 60
                    },
                    {
                        "VulLevel": 3,
                        "VulCount": 136
                    }
                ],
                "Score": 404
            },
            {
                "HostName": "临时概览页测试",
                "Quuid": "8092a54e-258d-45a1-ae1f-8477ee6d65fa",
                "VulLevelList": [
                    {
                        "VulLevel": 2,
                        "VulCount": 13
                    },
                    {
                        "VulLevel": 1,
                        "VulCount": 4
                    },
                    {
                        "VulLevel": 3,
                        "VulCount": 9
                    }
                ],
                "Score": 26
            },
            {
                "HostName": "交付同事使用__v_lwjlin",
                "Quuid": "928604de-876d-4c56-9914-6f53361944a5",
                "VulLevelList": [
                    {
                        "VulLevel": 2,
                        "VulCount": 13
                    },
                    {
                        "VulLevel": 1,
                        "VulCount": 4
                    },
                    {
                        "VulLevel": 3,
                        "VulCount": 9
                    }
                ],
                "Score": 26
            },
            {
                "HostName": "临时概览页测试",
                "Quuid": "a231448a-f7a5-4196-8a7e-30f5f6e9187e",
                "VulLevelList": [
                    {
                        "VulLevel": 2,
                        "VulCount": 13
                    },
                    {
                        "VulLevel": 1,
                        "VulCount": 3
                    },
                    {
                        "VulLevel": 3,
                        "VulCount": 9
                    }
                ],
                "Score": 25
            }
        ]
    }
}
```

