**Example 1: 修改采集规则配置**

FilterKeyRegex：Loglistener日志过滤规则列表（旧版），需要过滤日志的key，及其对应的regex。
 注意：2.9.3及以上版本LogListener ，建议使用AdvanceFilterRules配置日志过滤规则。


Input: 

```
tccli cls ModifyConfig --cli-unfold-argument  \
    --Path /data/log/**/my.log \
    --ExcludePaths.0.Type Path \
    --ExcludePaths.0.Value /data/log/my.log \
    --Name test2.8.8 \
    --LogType minimalist_log \
    --UserDefineRule  \
    --ExtractRule.IsGBK 0 \
    --ExtractRule.FilterKeyRegex.0.Key __CONTENT__ \
    --ExtractRule.FilterKeyRegex.0.Regex 400|500 \
    --ExtractRule.Backtracking 0 \
    --ExtractRule.MetadataType 2 \
    --ExtractRule.MetaTags.0.Key mryx \
    --ExtractRule.MetaTags.0.Value item \
    --ExtractRule.PathRegex  \
    --AdvancedConfig {"ClsAgentFileTimeout":3600} \
    --ConfigId a2c6342c-270a-4468-86cf-92625e466401
```

Output: 
```
{
    "Response": {
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

