**Example 1: 修改日志存储配置**

修改日志存储配置

Input: 

```
tccli cwp ModifyLogStorageConfig --cli-unfold-argument  \
    --Type malware \
    --Period 0 \
    --IsModifyPeriod True
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

