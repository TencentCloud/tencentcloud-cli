**Example 1: 修改采集规则配置**



Input: 

```
tccli cls ModifyConfig --cli-unfold-argument  \
    --ConfigId xxxxxx-xx-xx-xx-xxxxxxxx \
    --Name testname \
    --Path /data/nginx/log/access.log \
    --LogType delimiter_log \
    --ExtractRule.TimeKey date \
    --ExtractRule.TimeFormat %Y-%m-%d %H:%M:%S \
    --ExtractRule.Delimiter | \
    --ExtractRule.LogRegex .* \
    --ExtractRule.BeginRegex ^ \
    --ExtractRule.Keys date  content \
    --ExtractRule.FilterKeyRegex.0.Key xxx \
    --ExtractRule.FilterKeyRegex.0.Regex xxxx \
    --ExtractRule.UnMatchUpLoadSwitch True \
    --ExtractRule.UnMatchLogKey testlog \
    --ExtractRule.Backtracking 1048576 \
    --UserDefineRule xxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

