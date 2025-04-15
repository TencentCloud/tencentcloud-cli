**Example 1: DescribeNotebookSession**

查询交互式 session详情信息

Input: 

```
tccli dlc DescribeNotebookSession --cli-unfold-argument  \
    --SessionId d3018ad4-9a7e-4f64-a3f4-f38507c69742
```

Output: 
```
{
    "Response": {
        "RequestId": "********-****-****-****-7d00a55746d9",
        "Session": {
            "AppInfo": [],
            "Arguments": [
                {
                    "Key": "dlc.eni",
                    "Value": ""
                },
                {
                    "Key": "dlc.role.arn",
                    "Value": "00.1737099520.29eb837f.-.0.SPARK.00058.MTFiNWZmMDSPRH8hPPbkFHj1FdFTQTmwDnW7BR5i1THufNXmuXjyoQ=="
                }
            ],
            "CreateTime": "1737099521000",
            "DataEngineName": "cls-*******",
            "DriverSize": "small",
            "ExecutorMaxNumbers": 1,
            "ExecutorNumbers": 1,
            "ExecutorSize": "small",
            "Kind": "sql",
            "Name": "session1",
            "ProxyUser": "root",
            "ProgramArchives": null,
            "ProgramDependentFiles": null,
            "ProgramDependentJars": null,
            "ProgramDependentPython": null,
            "SessionId": "livy-session-***********",
            "SessionType": "",
            "SparkAppId": "spark-**********",
            "SparkUiUrl": "https://*******/jobs/",
            "State": "dead",
            "TimeoutInSecond": 90
        }
    }
}
```

