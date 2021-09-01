**Example 1: 创建采集规则配置**



Input: 

```
tccli cls CreateConfig --cli-unfold-argument  \
    --Name testname \
    --Path /data/nginx/log/**/access.log \
    --LogType delimiter_log \
    --ExtractRule.TimeKey date \
    --ExtractRule.TimeFormat %Y-%m-%d %H:%M:%S \
    --ExtractRule.Delimiter | \
    --ExtractRule.LogRegex .* \
    --ExtractRule.BeginRegex ^ \
    --ExtractRule.Keys date  content \
    --ExtractRule.FilterKeyRegex.0.Key xxx \
    --ExtractRule.FilterKeyRegex.0.Regex ssss \
    --ExtractRule.UnMatchLogKey testlog \
    --ExtractRule.UnMatchUpLoadSwitch True \
    --ExtractRule.Backtracking -1 \
    --ExcludePaths.0.Type xx \
    --ExcludePaths.0.Value xx \
    --Output xxxxxx-xxx-xxxxxx
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

