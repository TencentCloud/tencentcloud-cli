**Example 1: 查看智能运维配置**

查看智能运维配置

Input: 

```
tccli es GetDiagnoseSettings --cli-unfold-argument  \
    --InstanceId es-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "Status": 0,
        "Count": 0,
        "DiagnoseJobMetas": [
            {
                "JobZhName": "1",
                "JobDescription": "1",
                "JobName": "1"
            }
        ],
        "CronTime": "1",
        "RequestId": "1",
        "MaxCount": 0
    }
}
```

