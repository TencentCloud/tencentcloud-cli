**Example 1: 测试示例**

测试示例

Input: 

```
tccli tchousex DescribeEngineJobInfo --cli-unfold-argument  \
    --InstanceId warehouse-qiwlg758 \
    --EngineJobId batch-task-324ztz
```

Output: 
```
{
    "Response": {
        "InstanceId": "warehouse-qiwlg758",
        "ErrorMsg": "",
        "ExecuteUser": "test",
        "ExtParameters": [
            {
                "Name": "ClassName",
                "Value": "org.apache.spark.examples.SparkPi"
            },
            {
                "Name": "DriverCores",
                "Value": "1"
            },
            {
                "Name": "ExecutorCores",
                "Value": "1"
            },
            {
                "Name": "NumExecutors",
                "Value": "1"
            }
        ],
        "JobContent": "Y29zbjovL3lpaGFuZy1jcS1zcGFyay0xMzAxMDg3NDEzL3NwYXJrLWV4YW1wbGVzXzIuMTItMy4yLjMuamFy",
        "JobType": "jar",
        "JobUUID": "123",
        "RequestId": "1015ec08-76ce-44fb-bc19-2039398a44b4",
        "ResourcePath": ""
    }
}
```

