**Example 1: 部署容器应用**



Input: 

```
tccli tsf DeployContainerGroup --cli-unfold-argument  \
    --DoNotStart false \
    --MemRequest 1024 \
    --UpdateType 1 \
    --Server ccr.ccs.tencentyun.com \
    --InstanceNum 1 \
    --RepoName tsf_10000617xxxx/test \
    --TagName xxxx \
    --CpuRequest 0.54 \
    --JvmOpts -Xms128m-Xmx512m-XX:MetaspaceSize=128m-XX:MaxMetaspaceSize=512m \
    --UpdateIvl 10 \
    --GroupId group-xxxxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "b481cffd-6b00-463f-a1ae-7afe5fd5fa2e",
        "Result": true
    }
}
```

