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
            "JobName": "optimizer_job",
            "JobType": 1,
            "DataEngine": "DLC-engine",
            "Eni": "testeni2",
            "IsLocal": "cos",
            "JobFile": "cosn://danierwei-test-1305424723/sparkjar/spark-ckafka-1.0-SNAPSHOT.jar",
            "RoleArn": 3,
            "MainClass": "org.apache.spark.examples.SparkPi",
            "CmdArgs": "testArgs",
            "JobConf": "",
            "IsLocalJars": "cos",
            "JobJars": "lakefs://*/*/.system/sparkAppJar/20220513/*/spark-examples_2.12-3.1.2.jar",
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
            "SparkImageVersion": "",
            "SessionId": "xxssd-dsakjj-dkslk-doeks",
            "DataEngineClusterType": "spark_cu",
            "DataEngineImageVersion": "Spark 3.2",
            "IsInherit": 1,
            "IsSessionStarted": true
        },
        "IsExists": true,
        "RequestId": "2ae4707a-9f72-44aa-9fd4-65cb739d6301"
    }
}
```

