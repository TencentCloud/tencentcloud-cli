**Example 1: 查询智能运维诊断结果报告**

查询智能运维诊断结果报告

Input: 

```
tccli es DescribeDiagnose --cli-unfold-argument  \
    --InstanceId es-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "Total": 0,
        "DiagnoseResults": [
            {
                "JobResults": [
                    {
                        "Status": 0,
                        "MetricDetails": [
                            {
                                "Metrics": [
                                    {
                                        "Dimensions": [
                                            {
                                                "Value": "1",
                                                "Key": "1"
                                            }
                                        ],
                                        "Value": 0.0
                                    }
                                ],
                                "Key": "1"
                            }
                        ],
                        "Detail": "1",
                        "Summary": "1",
                        "SettingDetails": [
                            {
                                "Advise": "1",
                                "Value": "1",
                                "Key": "1"
                            }
                        ],
                        "Score": 0,
                        "Advise": "1",
                        "JobName": "1",
                        "LogDetails": [
                            {
                                "Count": 0,
                                "Advise": "1",
                                "Key": "1"
                            }
                        ]
                    }
                ],
                "InstanceId": "1",
                "Completed": true,
                "Score": 0,
                "RequestId": "1",
                "JobParam": {
                    "Indices": "1",
                    "Interval": 1,
                    "Jobs": [
                        "1"
                    ]
                },
                "CreateTime": "1",
                "JobType": 0
            }
        ],
        "RequestId": "1"
    }
}
```

