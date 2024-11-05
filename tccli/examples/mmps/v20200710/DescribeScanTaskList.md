**Example 1: 获取隐私合规诊断任务列表**



Input: 

```
tccli mmps DescribeScanTaskList --cli-unfold-argument  \
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
                "TaskID": "235414610411261952",
                "TaskType": 0,
                "TaskStatus": 0,
                "TaskErrMsg": "",
                "Source": 0,
                "AppInfo": {
                    "AppPackage": "wx66e50f1e*******6f",
                    "AppName": "测试app1",
                    "AppVersion": "v1.0",
                    "Platform": 2,
                    "ReportUrl": "诊断报告下载链接",
                    "ReportTitle": "诊断报告名称",
                    "BehaviorUrl": "诊断堆栈报告下载链接",
                    "BehaviorTitle": "诊断堆栈报告名称",
                    "HighRiskCount": 5,
                    "PrivacyTextName": "隐私申明文本.txt",
                    "SoftwareMD5": "c7991677cc********3f",
                    "PrivacyTextMD5": "3bc1efe919********23"
                },
                "StartTime": "2021-10-11 14:53:36",
                "EndTime": "2021-10-11 14:53:36",
                "ContactName": "张三"
            }
        ],
        "Total": 1
    }
}
```

