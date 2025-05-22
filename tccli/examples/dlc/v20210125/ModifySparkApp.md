**Example 1: 更新spark作业**



Input: 

```
tccli dlc ModifySparkApp --cli-unfold-argument  \
    --AppName jar_check_1 \
    --AppType 1 \
    --DataEngine thea_T282_spark_勿删 \
    --IsLocal lakefs \
    --AppFile lakefs://demo/1304581893/.system/sparkAppJar/20250519/be923656-33c0-4b6a-a4f8-814efb293f29/app-1.0-SNAPSHOT.jar \
    --IsLocalJars cos \
    --AppJars  \
    --IsLocalFiles cos \
    --AppArchives  \
    --IsLocalArchives cos \
    --AppFiles  \
    --IsLocalPythonFiles cos \
    --AppPythonFiles  \
    --RoleArn 1211 \
    --SparkImage  \
    --MainClass org.example.job.AppTest \
    --CmdArgs  \
    --AppConf  \
    --AppExecutorSize small \
    --AppDriverSize small \
    --AppExecutorNums 1 \
    --MaxRetries 1 \
    --DataSource  \
    --SessionId  \
    --AppExecutorMaxNumbers 1 \
    --IsInherit 0 \
    --SparkImageVersion  \
    --DependencyPackages.0.PackageSource Maven \
    --DependencyPackages.0.MavenPackage com.github.penfeizhou.android.animation:glide-plugin:3.0.5 \
    --IsSessionStarted False \
    --SparkAppId batch_776890ff-4f47-48e7-88ea-5c50c55c3866
```

Output: 
```
{
    "Response": {
        "RequestId": "d1e95669-101e-4d06-a9a7-c56d83f60b03"
    }
}
```

