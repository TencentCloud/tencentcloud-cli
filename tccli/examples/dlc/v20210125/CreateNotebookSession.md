**Example 1: 创建交互式session（notebook）**

创建交互式session（notebook）

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
        "SessionId": "abc",
        "SparkAppId": "abc",
        "State": "abc",
        "RequestId": "abc"
    }
}
```

