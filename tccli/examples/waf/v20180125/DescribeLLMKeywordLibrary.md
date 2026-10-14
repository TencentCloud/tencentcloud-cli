**Example 1: 查询关键词库列表（分页排序）**

按更新时间降序查询自定义词库列表，每页10条

Input: 

```
tccli waf DescribeLLMKeywordLibrary --cli-unfold-argument  \
    --Type custom \
    --Offset 0 \
    --Limit 10 \
    --By UpdateTime \
    --Order DESC
```

Output: 
```
{
    "Response": {
        "RequestId": "feca6493-7c4a-4103-a868-cc394d72ae8e",
        "LibList": [],
        "Total": 0
    }
}
```

