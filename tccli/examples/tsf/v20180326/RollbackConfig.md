**Example 1: 回滚配置**



Input: 

```
tccli tsf RollbackConfig --cli-unfold-argument  \
    --ConfigReleaseLogId dcfgrl-a2qj3qoa \
    --ReleaseDesc This is desc
```

Output: 
```
{
    "Response": {
        "RequestId": "78ee9cc9-b798-4596-961d-4391b6157ddf",
        "Result": true
    }
}
```

