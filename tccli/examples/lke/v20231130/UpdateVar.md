**Example 1: 更新变量**

更新变量

Input: 

```
tccli lke UpdateVar --cli-unfold-argument  \
    --AppBizId 1793260396881641472 \
    --VarId 55127e9e-6e9e-4c11-bcf8-b524959cd841 \
    --VarName TimeIDUpdate \
    --VarDesc 这个参数要来传时间 \
    --VarType STRING \
    --VarDefaultValue 2025-05-14 \
    --VarDefaultFileName 
```

Output: 
```
{
    "Response": {
        "RequestId": "94a2fb36-98dc-47d2-b39b-904d244ad888",
        "VarId": "55127e9e-6e9e-4c11-bcf8-b524959cd841"
    }
}
```

