**Example 1: 创建特殊采集配置任务**

创建特殊采集配置任务

Input: 

```
tccli cls CreateConfigExtra --cli-unfold-argument  \
    --Name configname \
    --TopicId 3269961d-52e0-407b-9dcd-34bd830c6f19 \
    --Type host_file \
    --HostFile.LogPath /var/log/tmep \
    --HostFile.FilePattern *.log \
    --HostFile.CustomLabels key1=value1 key2=value2 \
    --LogType minimalist_log \
    --ExtractRule.TimeKey date \
    --ExtractRule.TimeFormat %Y-%m-%d %H:%M:%S \
    --ExtractRule.Delimiter | \
    --ExtractRule.LogRegex .* \
    --ExtractRule.BeginRegex ^ \
    --ExtractRule.Keys date  content \
    --ExtractRule.FilterKeyRegex.0.Key __CONTENT__ \
    --ExtractRule.FilterKeyRegex.0.Regex 400|500 \
    --ExtractRule.UnMatchLogKey testlog \
    --ExtractRule.UnMatchUpLoadSwitch True \
    --ExtractRule.Backtracking -1 \
    --ExcludePaths.0.Type Path \
    --ExcludePaths.0.Value /var/log1/ \
    --ExcludePaths.1.Type File \
    --ExcludePaths.1.Value /var/log2/app.log \
    --UserDefineRule  \
    --GroupId 59b6014b-6507-44c2-9d4f-a5bee6df9ab5 \
    --ConfigFlag label_k8s \
    --LogsetId 0af7e6bb-fc91-4ee8-ad24-1129e9c91c6c \
    --LogsetName name1 \
    --TopicName name2
```

Output: 
```
{
    "Response": {
        "ConfigExtraId": "be923f41-dfbd-4a08-8afc-8b247647ae4b",
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

