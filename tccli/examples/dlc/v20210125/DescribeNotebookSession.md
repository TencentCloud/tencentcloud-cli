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
        "Session": {
            "Name": "abc",
            "Kind": "abc",
            "DataEngineName": "abc",
            "Arguments": [
                {
                    "Key": "abc",
                    "Value": "abc"
                }
            ],
            "ProgramDependentFiles": [
                "abc"
            ],
            "ProgramDependentJars": [
                "abc"
            ],
            "ProgramDependentPython": [
                "abc"
            ],
            "ProgramArchives": [
                "abc"
            ],
            "DriverSize": "abc",
            "ExecutorSize": "abc",
            "ExecutorNumbers": 1,
            "ProxyUser": "abc",
            "TimeoutInSecond": 0,
            "SparkAppId": "abc",
            "SessionId": "abc",
            "State": "abc",
            "CreateTime": "abc",
            "AppInfo": [
                {
                    "Key": "abc",
                    "Value": "abc"
                }
            ],
            "SparkUiUrl": "abc",
            "ExecutorMaxNumbers": 1
        },
        "RequestId": "abc"
    }
}
```

