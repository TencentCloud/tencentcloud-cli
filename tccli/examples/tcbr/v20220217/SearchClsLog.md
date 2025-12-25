**Example 1: pass**



Input: 

```
tccli tcbr SearchClsLog --cli-unfold-argument  \
    --Sort 字符串 \
    --EnvId 字符串 \
    --Context 字符串 \
    --UseLucene false \
    --QueryString 字符串 \
    --Limit 1 \
    --StartTime 字符串 \
    --EndTime 字符串
```

Output: 
```
{
    "Response": {
        "LogResults": {
            "Context": "",
            "ListOver": false,
            "Results": null
        },
        "RequestId": "e5c883fb-ca6a-4481-9f3d-d28ebfee50c3"
    }
}
```

**Example 2: 搜索CLS日志**



Input: 

```
tccli tcbr SearchClsLog --cli-unfold-argument  \
    --EnvId env-id \
    --StartTime 2006-01-02 03:04:05 \
    --EndTime 2006-01-02 03:04:05 \
    --QueryString QueryString \
    --Context Context \
    --Limit 1 \
    --Sort Sort \
    --UseLucene True
```

Output: 
```
{
    "Response": {
        "RequestId": "3e22b381-93a3-44c4-85b7-456679a7b8cd",
        "LogResults": {
            "Context": "",
            "ListOver": true,
            "Results": []
        }
    }
}
```

