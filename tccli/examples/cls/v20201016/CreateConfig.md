**Example 1: 创建采集规则配置**

创建采集规则配置

Input: 

```
tccli cls CreateConfig --cli-unfold-argument  \
    --Name abc \
    --Path abc \
    --LogType abc \
    --ExtractRule.TimeKey abc \
    --ExtractRule.TimeFormat abc \
    --ExtractRule.Delimiter abc \
    --ExtractRule.LogRegex abc \
    --ExtractRule.BeginRegex abc \
    --ExtractRule.Keys abc \
    --ExtractRule.FilterKeyRegex.0.Key abc \
    --ExtractRule.FilterKeyRegex.0.Regex abc \
    --ExtractRule.UnMatchUpLoadSwitch True \
    --ExtractRule.UnMatchLogKey abc \
    --ExtractRule.Backtracking 0 \
    --ExtractRule.IsGBK 0 \
    --ExtractRule.JsonStandard 0 \
    --ExtractRule.Protocol abc \
    --ExtractRule.Address abc \
    --ExtractRule.ParseProtocol abc \
    --ExtractRule.MetadataType 0 \
    --ExtractRule.PathRegex abc \
    --ExtractRule.MetaTags.0.Key abc \
    --ExtractRule.MetaTags.0.Value abc \
    --ExcludePaths.0.Type abc \
    --ExcludePaths.0.Value abc \
    --Output abc \
    --UserDefineRule abc \
    --AdvancedConfig abc
```

Output: 
```
{
    "Response": {
        "ConfigId": "xxxx-xx-xx-xx-xxxxxxxx",
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

