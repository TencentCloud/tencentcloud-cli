**Example 1: 创建变量**

创建变量

Input: 

```
tccli lke CreateVar --cli-unfold-argument  \
    --AppBizId 1793260396881641472 \
    --VarName TimeID \
    --VarDesc 这个参数要来传时间 \
    --VarType STRING \
    --VarDefaultValue 2025-05-14 \
    --VarDefaultFileName 
```

Output: 
```
{
    "Response": {
        "RequestId": "aa7b90b3-bca5-4666-8bb8-e76b0374137c",
        "VarId": "55127e9e-6e9e-4c11-bcf8-b524959cd841"
    }
}
```

