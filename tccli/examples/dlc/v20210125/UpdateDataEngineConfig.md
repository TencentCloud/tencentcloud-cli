**Example 1: 更新指定引擎的结果桶配置信息**

更新指定引擎的结果桶配置信息

Input: 

```
tccli dlc UpdateDataEngineConfig --cli-unfold-argument  \
    --DataEngineIds DataEngine-xxx \
    --DataEngineConfigCommand UpdateSparkSQLResultPath
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

