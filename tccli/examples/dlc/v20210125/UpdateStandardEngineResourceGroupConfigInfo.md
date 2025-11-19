**Example 1: 增加指定配置到资源组**

增加指定配置到资源组

Input: 

```
tccli dlc UpdateStandardEngineResourceGroupConfigInfo --cli-unfold-argument  \
    --EngineResourceGroupName test-rg \
    --UpdateConfContext.0.ConfigType StaticConfigType \
    --UpdateConfContext.0.Params.0.ConfigItem spark.sql.shuffle.partitions \
    --UpdateConfContext.0.Params.0.ConfigValue 300 \
    --UpdateConfContext.0.Params.0.Operate ADD \
    --IsEffectiveNow 1
```

Output: 
```
{
    "Response": {
        "RequestId": "6e844f50-46ae-422f-882c-e8f6c67cff13"
    }
}
```

