**Example 1: 生成提取K-V格式日志的正则表达式**



Input: 

```
tccli cls GenKVRegex --cli-unfold-argument  \
    --LogSample log text \
    --Indexes.0.Start 0 \
    --Indexes.0.End 1
```

Output: 
```
{
    "Response": {
        "Regex": "\\w+xxxx.",
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

