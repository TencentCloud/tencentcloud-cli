**Example 1: 获取应用合规诊断任务列表**



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
                "TaskID": "1701438134******0",
                "TaskType": "0",
                "TaskStatus": "0",
                "TaskErrMsg": "内部错误",
                "Source": "2",
                "AppInfo": {
                    "AppPackage": "com.test.app",
                    "AppName": "测试App",
                    "AppVersion": "v1.0",
                    "Platform": "0",
                    "ReportUrl": "诊断报告下载链接",
                    "ReportTitle": "诊断报告名称",
                    "BehaviorUrl": "诊断堆栈报告下载链接",
                    "BehaviorTitle": "诊断堆栈报告名称",
                    "HighRiskCount": "5",
                    "PrivacyTextName": "隐私申明文本.txt",
                    "SoftwareMD5": "c7991677cc57d3b9d4974316db0ac4f9f430593f",
                    "PrivacyTextMD5": "3bc1efe919a5245f711071373a2b4523"
                },
                "StartTime": "2021-09-30 10:57:34",
                "EndTime": "2021-10-11 14:53:36",
                "ContactName": "老王"
            }
        ],
        "Total": 1
    }
}
```

