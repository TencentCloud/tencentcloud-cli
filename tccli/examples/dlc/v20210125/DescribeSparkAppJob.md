**Example 1: 查询具体的spark应用**



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
        "RequestId": "2ae4707a-9f72-44aa-9fd4-65cb739d6301",
        "Job": {
            "JobId": "batch_e6c5ae75-fb02-4831-a5b8-88999d09003c",
            "JobType": 1,
            "CmdArgs": "",
            "CurrentTaskId": "",
            "DataEngine": "testjar3",
            "Eni": "testeni2",
            "IsLocal": "cos",
            "IsLocalFiles": "lakefs",
            "IsLocalJars": "lakefs",
            "JobConf": "",
            "JobCreateTime": 1652442914350,
            "JobCreator": "100019868890",
            "JobDriverSize": "small",
            "JobExecutorNums": 1,
            "JobExecutorSize": "small",
            "JobFile": "cosn://danierwei-test-1305424723/sparkjar/spark-ckafka-1.0-SNAPSHOT.jar",
            "JobFiles": "",
            "JobJars": "lakefs://4000002928ef2638d7ab6aabb088bd51b7db914729a5c43b13a998ffa9750511f511d0ab@dlcda57-100018379117-1636704841-100017307912-1304028854/1305424723/.system/sparkAppJar/20220513/dd3c6ad3-a746-40d8-806c-fa8b15b5e9f9/spark-examples_2.12-3.1.2.jar",
            "JobMaxAttempts": 1,
            "JobName": "andy_test",
            "JobUpdateTime": 1652769991248,
            "MainClass": "org.apache.spark.examples.SparkPi",
            "RoleArn": 3
        },
        "IsExists": true
    }
}
```

