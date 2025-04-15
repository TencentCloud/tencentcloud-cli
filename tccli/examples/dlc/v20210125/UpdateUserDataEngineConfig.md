**Example 1: 修改用户集群自定义配置**

修改用户集群自定义配置

Input: 

```
tccli dlc UpdateUserDataEngineConfig --cli-unfold-argument  \
    --DataEngineId DataEngine-xxxx \
    --DataEngineConfigPairs.0.ConfigItem eos.sql.processType \
    --DataEngineConfigPairs.0.ConfigValue DIRECT \
    --SessionResourceTemplate.DriverSize small \
    --SessionResourceTemplate.ExecutorSize small \
    --SessionResourceTemplate.ExecutorNums 1 \
    --SessionResourceTemplate.ExecutorMaxNumbers 1
```

Output: 
```
{
    "Response": {
        "RequestId": "32157dff-hhd6-4d9e-ba9e"
    }
}
```

