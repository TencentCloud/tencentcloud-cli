**Example 1: 查询session信息**



Input: 

```
tccli tchousex DescribeSparkAllSessions --cli-unfold-argument  \
    --InstanceId instance-s4ukwjv7 \
    --Offset 0 \
    --Limit 10 \
    --CreateTimeOrder desc
```

Output: 
```
{
    "Response": {
        "RequestId": "79a55bce-58a6-4e7c-97ec-4a7531971fda",
        "ErrorMsg": "",
        "SparkSessionList": [
            {
                "InstanceId": "instance-liyit2c1",
                "SessionId": "livy-session-9xld7dwg",
                "Name": "session-1747133085",
                "Kind": "pyspark",
                "Jars": "",
                "PyFiles": "",
                "Files": "",
                "Archives": "",
                "State": "dead",
                "ExecutorCores": 4,
                "ExecutorNum": 1,
                "DriverCores": 8,
                "SparkUiUrl": "https://tchouse-x-spark-ui.beijing.cloud.tencent.com/history/spark-397c2e98a8ad498db4e649c6159f4646/none/none/jobs/",
                "TimeoutInSecond": 3600,
                "DriverPodName": "",
                "ExecutorPodNames": "",
                "Source": 1,
                "ExecuteTime": "63min22s",
                "Creator": "100038834829",
                "BeginTime": "2025-05-13 18:45:14",
                "UserName": "root",
                "Configs": "spark.xxx=true\nspark.xx1=0"
            },
            {
                "InstanceId": "instance-liyit2c1",
                "SessionId": "livy-session-shwewn4i",
                "Name": "session-1745205370",
                "Kind": "pyspark",
                "Jars": "",
                "PyFiles": "",
                "Files": "",
                "Archives": "",
                "State": "dead",
                "ExecutorCores": 4,
                "ExecutorNum": 1,
                "DriverCores": 8,
                "SparkUiUrl": "https://tchouse-x-spark-ui.beijing.cloud.tencent.com/history/spark-33b1f739329e4bd0a11c2039e0f1912b/none/none/jobs/",
                "TimeoutInSecond": 3600,
                "DriverPodName": "",
                "ExecutorPodNames": "",
                "Source": 1,
                "ExecuteTime": "62min44s",
                "Creator": "100038834829",
                "BeginTime": "2025-04-21 11:16:28",
                "UserName": "root",
                "Configs": "spark.xxx=true\nspark.xx1=0"
            },
            {
                "InstanceId": "instance-liyit2c1",
                "SessionId": "livy-session-25kvme9q",
                "Name": "session-1744970541",
                "Kind": "pyspark",
                "Jars": "",
                "PyFiles": "",
                "Files": "",
                "Archives": "",
                "State": "dead",
                "ExecutorCores": 4,
                "ExecutorNum": 1,
                "DriverCores": 8,
                "SparkUiUrl": "https://tchouse-x-spark-ui.beijing.cloud.tencent.com/history/spark-c3b5d47b6d184697b79263bf94058ae8/none/none/jobs/",
                "TimeoutInSecond": 3600,
                "DriverPodName": "",
                "ExecutorPodNames": "",
                "Source": 1,
                "ExecuteTime": "61min56s",
                "Creator": "100038834829",
                "BeginTime": "2025-04-18 18:03:15",
                "UserName": "root",
                "Configs": "spark.xxx=true\nspark.xx1=0"
            }
        ],
        "TotalCount": 3
    }
}
```

