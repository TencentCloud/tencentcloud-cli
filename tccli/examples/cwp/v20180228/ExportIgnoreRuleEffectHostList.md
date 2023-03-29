**Example 1: 导出忽略检测项影响主机列表**

根据忽略检测项id导出影响主机列表数据

Input: 

```
tccli cwp ExportIgnoreRuleEffectHostList --cli-unfold-argument  \
    --RuleId 1
```

Output: 
```
{
    "Response": {
        "DownloadUrl": "",
        "TaskId": "12312",
        "RequestId": "abc"
    }
}
```

