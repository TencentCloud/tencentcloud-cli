**Example 1: 创建单行全文**

FilterKeyRegex：Loglistener日志过滤规则列表（旧版），需要过滤日志的key，及其对应的regex。
 注意：2.9.3及以上版本LogListener ，建议使用AdvanceFilterRules配置日志过滤规则。


Input: 

```
tccli cls CreateConfig --cli-unfold-argument  \
    --Name test2.8.8 \
    --Path /data/log/**/my.log \
    --LogType minimalist_log \
    --UserDefineRule  \
    --ExtractRule.IsGBK 0 \
    --ExtractRule.FilterKeyRegex.0.Key __CONTENT__ \
    --ExtractRule.FilterKeyRegex.0.Regex 400|500 \
    --ExtractRule.Backtracking 0 \
    --ExtractRule.MetadataType 0 \
    --ExtractRule.MetaTags.0.Key  \
    --ExtractRule.MetaTags.0.Value  \
    --ExtractRule.PathRegex  \
    --AdvancedConfig {"ClsAgentFileTimeout":0} \
    --Output 6bf3355c-3c88-4566-89c8-76c3ca37bae9
```

Output: 
```
{
    "Response": {
        "ConfigId": "a2c6342c-270a-4468-86cf-92625e468888",
        "RequestId": "a21b16c1-4da9-45a1-a612-59e5757384f3"
    }
}
```

**Example 2: 创建组合解析配置**

创建组合解析配置

Input: 

```
tccli cls CreateConfig --cli-unfold-argument  \
    --Name my-test \
    --Path /data/log/**/my.log \
    --LogType user_define_log \
    --UserDefineRule {"processors":[{"type":"processor_split_delimiter","detail":{"Delimiter":",","ExtractKeys":["time","msg1","msg2"]},"processors":[{"type":"processor_timeformat","detail":{"KeepSource":true,"TimeFormat":"%s","SourceKey":"time"}},{"type":"processor_split_delimiter","detail":{"KeepSource":false,"Delimiter":"|","SourceKey":"msg1","ExtractKeys":["submsg1","submsg2","submsg3"]},"processors":[]},{"type":"processor_split_key_value","detail":{"KeepSource":false,"Delimiter":"：","SourceKey":"msg2"}}]}]} \
    --ExtractRule.IsGBK 0 \
    --ExtractRule.UnMatchUpLoadSwitch True \
    --ExtractRule.UnMatchLogKey LogParseFailure \
    --ExtractRule.Backtracking 0 \
    --ExtractRule.MetadataType 2 \
    --ExtractRule.MetaTags.0.Key mryx \
    --ExtractRule.MetaTags.0.Value item \
    --ExtractRule.PathRegex  \
    --AdvancedConfig {"ClsAgentFileTimeout":3600} \
    --Output 6bf3355c-3c88-4566-89c8-76c3ca37bae9
```

Output: 
```
{
    "Response": {
        "ConfigId": "d72dae22-084c-4d20-a81b-f42e25c88888",
        "RequestId": "c708e9af-231e-4a94-a888-3ab24e5fbd97"
    }
}
```

**Example 3: 创建采集规则配置**

创建采集规则配置

Input: 

```
tccli cls CreateConfig --cli-unfold-argument  \
    --Name my-test-minimalist_log \
    --Path /data/log/**/my.log \
    --ExcludePaths.0.Type File \
    --ExcludePaths.0.Value /data/log/mryx/my.log \
    --LogType minimalist_log \
    --UserDefineRule  \
    --ExtractRule.IsGBK 0 \
    --ExtractRule.Backtracking 0 \
    --ExtractRule.MetadataType 2 \
    --ExtractRule.MetaTags.0.Key mryx \
    --ExtractRule.MetaTags.0.Value item \
    --ExtractRule.MetaTags.1.Key wd \
    --ExtractRule.MetaTags.1.Value shop \
    --ExtractRule.PathRegex  \
    --AdvancedConfig {"ClsAgentMaxDepth":10} \
    --Output 6bf3355c-3c88-4566-89c8-76c3ca37bae9
```

Output: 
```
{
    "Response": {
        "ConfigId": "b5a78efe-984c-47e2-99a8-52dbd1388888",
        "RequestId": "037a6def-51d4-449b-a894-7cd2410bfae1"
    }
}
```

**Example 4: 创建单行完全正则-文件日志**



Input: 

```
tccli cls CreateConfig --cli-unfold-argument  \
    --Name 单行完全正则-文件日志 \
    --Path /data/log/**/my.log \
    --ExcludePaths.0.Type File \
    --ExcludePaths.0.Value /data/log/my.log \
    --LogType fullregex_log \
    --UserDefineRule  \
    --ExtractRule.IsGBK 0 \
    --ExtractRule.BeginRegex \{"\w+":"\w+","\w+":"\w+","\w+":\{"\w+"[^"]+([^,]+),"\w+":"/\w+/\w+/\*\*/\w+\.\w+","\w+":\[\{"\w+":"\w+","\w+":"/\w+/\w+/\w+\.\w+"\}\],"\w+":"\w+\.\d+\.\d+","\w+":"\w+","\w+":"\w+","\w+":"","\w+":\{"\w+":\d+,"\w+":\[\{"\w+":"\w+","\w+":"\d+\|\d+"\}\],"\w+":\d+,"\w+":\d+,"\w+":\[\{"\w+":"\w+","\w+":"\w+"\}\],"\w+":"","\w+":\[\]\},"\w+":"\{\\"\w+\\":\d+\}","\w+"[^"]+([^\}]+).* \
    --ExtractRule.LogRegex \{"\w+":"\w+","\w+":"\w+","\w+":\{"\w+"[^"]+([^,]+),"\w+":"/\w+/\w+/\*\*/\w+\.\w+","\w+":\[\{"\w+":"\w+","\w+":"/\w+/\w+/\w+\.\w+"\}\],"\w+":"\w+\.\d+\.\d+","\w+":"\w+","\w+":"\w+","\w+":"","\w+":\{"\w+":\d+,"\w+":\[\{"\w+":"\w+","\w+":"\d+\|\d+"\}\],"\w+":\d+,"\w+":\d+,"\w+":\[\{"\w+":"\w+","\w+":"\w+"\}\],"\w+":"","\w+":\[\]\},"\w+":"\{\\"\w+\\":\d+\}","\w+"[^"]+([^\}]+).* \
    --ExtractRule.Keys Version ConfigId \
    --ExtractRule.TimeKey log_time \
    --ExtractRule.TimeFormat %Y-%m-%d %H:%M:%S.%f \
    --ExtractRule.FilterKeyRegex.0.Key key1 \
    --ExtractRule.FilterKeyRegex.0.Regex value1 \
    --ExtractRule.FilterKeyRegex.1.Key key2 \
    --ExtractRule.FilterKeyRegex.1.Regex velue2 \
    --ExtractRule.UnMatchUpLoadSwitch True \
    --ExtractRule.UnMatchLogKey LogParseFailure \
    --ExtractRule.Backtracking 10 \
    --ExtractRule.MetadataType 2 \
    --ExtractRule.MetaTags.0.Key mryx \
    --ExtractRule.MetaTags.0.Value item \
    --ExtractRule.PathRegex  \
    --AdvancedConfig {"ClsAgentMaxDepth":10,"ClsAgentFileTimeout":3600} \
    --Output 6bf3355c-3c88-4566-89c8-76c3ca37bae9
```

Output: 
```
{
    "Response": {
        "ConfigId": "8e63fe9a-5f36-49b0-bdbf-ab1c29e58888",
        "RequestId": "420f4f07-2134-4167-9442-9ac6c6ffe3d8"
    }
}
```

