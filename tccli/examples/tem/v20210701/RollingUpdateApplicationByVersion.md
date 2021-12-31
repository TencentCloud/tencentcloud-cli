**Example 1: 应用部署**

应用部署

Input: 

```
tccli tem RollingUpdateApplicationByVersion --cli-unfold-argument  \
    --ApplicationId xx \
    --EnvironmentId xx \
    --DeployVersion xx \
    --PackageName xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "81f74023-563c-437d-abf7-8139449ef178",
        "Result": "version-xxx"
    }
}
```

