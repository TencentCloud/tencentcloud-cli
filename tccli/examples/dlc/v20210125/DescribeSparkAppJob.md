**Example 1: 查询spark作业信息**

查询spark作业信息

Input: 

```
tccli dlc DescribeSparkAppJob --cli-unfold-argument  \
    --JobId batch_133e005d-6486-4517-8ea7-b6b97b183a6b \
    --JobName spark_app
```

Output: 
```
{
    "Response": {
        "Job": {
            "JobId": "batch_e6c5ae75-fb02-4831-a5b8-88999d09003c",
            "JobName": "abc",
            "JobType": 1,
            "DataEngine": "testjar3",
            "Eni": "testeni2",
            "IsLocal": "cos",
            "JobFile": "cosn://danierwei-test-1305424723/sparkjar/spark-ckafka-1.0-SNAPSHOT.jar",
            "RoleArn": 3,
            "MainClass": "org.apache.spark.examples.SparkPi",
            "CmdArgs": "testArgs",
            "JobConf": "",
            "IsLocalJars": "abc",
            "JobJars": "lakefs://4000002928ef2638d7ab6aabb088bd51b7db914729a5c43b13a998ffa9750511f511d0ab@dlcda57-100018379117-1636704841-100017307912-1304028854/1305424723/.system/sparkAppJar/20220513/dd3c6ad3-a746-40d8-806c-fa8b15b5e9f9/spark-examples_2.12-3.1.2.jar",
            "IsLocalFiles": "lakefs",
            "JobFiles": "",
            "JobDriverSize": "small",
            "JobExecutorSize": "small",
            "JobExecutorNums": 1,
            "JobMaxAttempts": 1,
            "JobCreator": "admin",
            "JobCreateTime": 1652769991248,
            "JobUpdateTime": 1652769991248,
            "CurrentTaskId": "2aedsa7a-9ds2-44ds-9fdd-65cbds9d6301",
            "JobStatus": 1,
            "StreamingStat": {
                "StartTime": "2022-01-01 12:12:12",
                "Receivers": 0,
                "NumActiveReceivers": 0,
                "NumInactiveReceivers": 0,
                "NumActiveBatches": 0,
                "NumRetainedCompletedBatches": 0,
                "NumTotalCompletedBatches": 0,
                "AverageInputRate": 0,
                "AverageSchedulingDelay": 0,
                "AverageProcessingTime": 0,
                "AverageTotalDelay": 0
            },
            "DataSource": "DataLakeCatalog",
            "IsLocalPythonFiles": "cos",
            "AppPythonFiles": "cosn://xxx",
            "IsLocalArchives": "cos",
            "JobArchives": "cosn://xxx",
            "SparkImage": "Spark3.2",
            "JobPythonFiles": "cos",
            "TaskNum": 1,
            "DataEngineStatus": 0,
            "JobExecutorMaxNumbers": 1,
            "SparkImageVersion": "abc",
            "SessionId": "xxssd-dsakjj-dkslk-doeks",
            "DataEngineClusterType": "abc",
            "DataEngineImageVersion": "abc",
            "IsInherit": 1,
            "IsSessionStarted": true
        },
        "IsExists": true,
        "RequestId": "2ae4707a-9f72-44aa-9fd4-65cb739d6301"
    }
}
```

