**Example 1: 获取诊断任务为空的情况**



Input: 

```
tccli acp DescribeScanTaskList --cli-unfold-argument  \
    --TaskStatuses 0,1,2 \
    --PageSize 10 \
    --PageNo 1 \
    --Platform 0 \
    --TaskTypes 0,1 \
    --Source -1
```

Output: 
```
{
    "Response": {
        "RequestId": "e7c3b1d4-a45b-4a45-be38-49565552a871",
        "Result": 0,
        "Total": 0,
        "Data": null
    }
}
```

**Example 2: 获取应用合规诊断任务列表**



Input: 

```
tccli acp DescribeScanTaskList --cli-unfold-argument  \
    --TaskStatuses "0,1,2" \
    --PageNo 0 \
    --PageSize 10 \
    --TaskTypes "0,1" \
    --Source -1 \
    --Platform 2
```

Output: 
```
{
    "Response": {
        "RequestId": "5e93a212-ca01-0fdc-eedd-5a1fce5e83e6",
        "Result": 0,
        "Data": [
            {
                "TaskID": "235***952",
                "TaskType": 0,
                "TaskStatus": 0,
                "TaskErrMsg": "",
                "Source": 0,
                "AppInfo": {
                    "AppPackage": "wx66e50f1e*******6f",
                    "AppName": "测试app1",
                    "AppVersion": "v1.0",
                    "Platform": 2,
                    "ReportUrl": "",
                    "ReportTitle": "",
                    "BehaviorUrl": "",
                    "BehaviorTitle": ""
                },
                "StartTime": "2021-10-11 14:53:36",
                "EndTime": "2021-10-11 14:53:36"
            }
        ],
        "Total": 1
    }
}
```

