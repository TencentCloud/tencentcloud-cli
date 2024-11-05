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
        "DownloadUrl": "https://cwp-1258344***.cos.ap-guangzhou.myqcloud.com/file.txt",
        "TaskId": "12312",
        "RequestId": "d73d4495-1895-43a8-95be-f447b02e253d"
    }
}
```

