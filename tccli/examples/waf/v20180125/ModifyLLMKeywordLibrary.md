**Example 1: 修改自定义词库**

用户修改自定义词库内容

Input: 

```
tccli waf ModifyLLMKeywordLibrary --cli-unfold-argument  \
    --LibList.0.Name lib1 \
    --LibList.0.Description this is lib 1 \
    --LibList.0.Type custom \
    --LibList.0.Keywords word1
```

Output: 
```
{
    "Response": {
        "RequestId": "feca6493-7c4a-4103-a868-cc394d72ae8e",
        "RuleIds": [
            "5200027919"
        ]
    }
}
```

