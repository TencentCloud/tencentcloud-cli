**Example 1: 创建交互式session**



Input: 

```
tccli tchousex CreateNotebookSession --cli-unfold-argument  \
    --Name session-1737346629 \
    --Kind spark \
    --InstanceId warehouse-hk9pr4ve \
    --Files  \
    --Jars  \
    --PyFiles  \
    --Archives  \
    --DriverCores 4 \
    --ExecutorCores 4 \
    --ExecutorNum 1 \
    --TimeoutInSecond 3600
```

Output: 
```
{
    "Response": {
        "RequestId": "9a4b946f-3f2b-4311-b6fc-602134208437",
        "ErrorMsg": "",
        "SparkAppId": "",
        "State": "starting",
        "SessionId": "livy-session-l5dkp5"
    }
}
```

