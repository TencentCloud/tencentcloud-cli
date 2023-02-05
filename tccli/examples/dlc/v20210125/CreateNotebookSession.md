**Example 1: 创建notebook livy session**

创建notebook session

Input: 

```
tccli dlc CreateNotebookSession --cli-unfold-argument  \
    --Kind spark \
    --Name session1 \
    --ProxyUser root \
    --ProgramDependentPython cosn://xxx \
    --ProgramDependentFiles cosn://xxx \
    --ExecutorSize small \
    --ExecutorNumbers 1 \
    --ExecutorMaxNumbers 1 \
    --DataEngineName data_engine_1 \
    --ProgramDependentJars cosn://xxx \
    --Arguments.0.Value eni \
    --Arguments.0.Key test_eni \
    --TimeoutInSecond 3600 \
    --ProgramArchives cosn://xxx \
    --DriverSize small
```

Output: 
```
{
    "Response": {
        "SparkAppId": "xx",
        "SessionId": "d3018ad4-9a7e-4f64-a3f4-f38507c69742",
        "State": "not_started",
        "RequestId": "b8sd7dd7-ekd4-4e5e-993e-e5db64fa21c1"
    }
}
```

