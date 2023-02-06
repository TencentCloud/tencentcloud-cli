**Example 1: DescribeNotebookSession**

查询Session详情。

Input: 

```
tccli dlc DescribeNotebookSession --cli-unfold-argument  \
    --SessionId d3018ad4-9a7e-4f64-a3f4-f38507c69742
```

Output: 
```
{
    "Response": {
        "Session": {
            "DriverSize": "small",
            "Kind": "spark",
            "Name": "session1",
            "SparkUiUrl": "xx",
            "ProxyUser": "root",
            "CreateTime": "2006-01-02 15:04:05",
            "ProgramDependentPython": [
                "cosn://xxx"
            ],
            "ProgramDependentFiles": [
                "cosn://xxx"
            ],
            "ExecutorSize": "small",
            "SessionId": "d3018ad4-9a7e-4f64-a3f4-f38507c69742",
            "ExecutorNumbers": 1,
            "ExecutorMaxNumbers": 1,
            "DataEngineName": "data_engine_1",
            "ProgramDependentJars": [
                "cosn://xxx"
            ],
            "SparkAppId": "spark-4ke6a46618d24e9c7yh2b62f0ddebdks",
            "TimeoutInSecond": 3600,
            "AppInfo": [
                {
                    "Value": "",
                    "Key": ""
                }
            ],
            "State": "not_started",
            "ProgramArchives": [
                "cosn://xxx"
            ],
            "Arguments": [
                {
                    "Value": "eni",
                    "Key": "test_eni"
                }
            ]
        },
        "RequestId": "b8sd7dd7-ekd4-4e5e-993e-e5db64fa21c1"
    }
}
```

