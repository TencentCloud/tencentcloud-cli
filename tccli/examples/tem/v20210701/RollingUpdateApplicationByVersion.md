**Example 1: 应用部署**

应用部署

Input: 

```
tccli tem RollingUpdateApplicationByVersion --cli-unfold-argument  \
    --ApplicationId app-xxxxxx \
    --EnvironmentId en-xxxxxx \
    --DeployVersion v1 \
    --PackageName test.jar \
    --From IntelliJ \
    --DeployStrategyType 0 \
    --TotalBatchCount 0 \
    --BatchInterval 0 \
    --BetaBatchNum 0 \
    --MinAvailable 0 \
    --Force True
```

Output: 
```
{
    "Response": {
        "RequestId": "81f74023-563c-437d-abf7-8139449ef178",
        "Result": "revision-xxx"
    }
}
```

**Example 2: 部署成功**

部署成功

Input: 

```
tccli tem RollingUpdateApplicationByVersion --cli-unfold-argument  \
    --EnvironmentId env-qgnzgy8r \
    --TotalBatchCount 2 \
    --PackageName tem/pkg/1300555551/service-gn54vdy6/1641528220867/hello-world-0.0.1-SNAPSHOT.jar \
    --DeployStrategyType AUTO \
    --DeployVersion 20220107122452 \
    --BatchInterval 60 \
    --ApplicationId service-gn54vdy6 \
    --BetaBatchNum 1
```

Output: 
```
{
    "Response": {
        "RequestId": "28fe46b2-dbd9-4ee6-b388-603acb6c9263",
        "Result": ""
    }
}
```

