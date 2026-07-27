**Example 1: 更新tdlc spark作业**



Input: 

```
tccli dlc ModifySparkAppForTDLC --cli-unfold-argument  \
    --AppName test119 \
    --AppType 1 \
    --DataEngine test01 \
    --AppFile lakefs://********************463247dbed0b3a1342652f033ad2d5e7dc673535b4e9bfd0ac8b@dl************************************************************************************026071****************************************************************************** \
    --RoleArn 1124 \
    --AppDriverSize medium \
    --AppExecutorSize medium \
    --AppExecutorNums 1 \
    --SparkAppId batch_e5648d1b-a626-439d-af4b-ea405b9da7a6 \
    --Eni eni-12345678 \
    --IsLocal lakefs \
    --MainClass com.tencent.dlc.Test \
    --AppConf spark.network.timeout=120s
spark.sql.shuffle.partitions=200 \
    --IsLocalJars cos \
    --AppJars cosn://dlc-bucket001/jars/spark-sql-kafka-connector.jar \
    --IsLocalFiles cos \
    --AppFiles cosn://dlc-bucket001/files/config.properties \
    --IsLocalPythonFiles cos \
    --AppPythonFiles  \
    --CmdArgs 4 \
    --MaxRetries 5 \
    --DataSource DataLakeCatalog \
    --IsLocalArchives cos \
    --AppArchives cosn://dlc-bucket001/archives/venv.tar.gz \
    --SparkImage 1.1.0 \
    --SparkImageVersion Spark 3.2.1.3 \
    --AppExecutorMaxNumbers 7 \
    --SessionId 550e8400-e29b-41d4-a716-446655440000 \
    --IsInherit 0 \
    --IsSessionStarted False \
    --DependencyPackages.0.PackageSource CosOrFile \
    --DependencyPackages.0.PackageType pymodules \
    --DependencyPackages.0.PackagePath lakefs://********************463247dbed0b3a1342652f033ad2d5e7dc673535b4e9*************************************************************************/.system/sparkAppJar/2026071***********************f********************
```

Output: 
```
{
    "Response": {
        "RequestId": "367f6eb3-bce0-470d-8b79-093e4fcc686e"
    }
}
```

