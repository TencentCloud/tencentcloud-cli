**Example 1: 部署容器应用**



Input: 

```
tccli tsf DeployContainerGroup --cli-unfold-argument  \
    --GroupId group-xxxxxxx \
    --CpuRequest 0.54 \
    --MemRequest 1024 \
    --Server ccr.ccs.tencentyun.com \
    --RepoName tsf_10000617xxxx/test \
    --TagName xxxx \
    --DoNotStart false \
    --InstanceNum 1 \
    --JvmOpts -Xms128m-Xmx512m-XX:MetaspaceSize \
    --UpdateType 1 \
    --UpdateIvl 10
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

