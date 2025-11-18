**Example 1: 修改应用配置**

修改应用配置

Input: 

```
tccli apm ModifyApmApplicationConfig --cli-unfold-argument  \
    --InstanceId apm-1o8yMC47u \
    --ServiceName java-market-service11 \
    --ExceptionFilter stock(.*?),ppp(.*?) \
    --UrlConvergence stock(.*?),ppp(.*?) \
    --ErrorCodeFilter 500,400 \
    --UrlConvergenceSwitch 1 \
    --UrlConvergenceThreshold 500 \
    --UrlExclude 33132 \
    --EnableSnapshot False \
    --SnapshotTimeout 2000
```

Output: 
```
{
    "Response": {
        "RequestId": "wcl-9esoxoii8t2exer215won26rkzc8"
    }
}
```

