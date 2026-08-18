**Example 1: 创建视图**



Input: 

```
tccli cloudrc CreateView --cli-unfold-argument  \
    --ViewName 广州地域视图 \
    --Filters.0.Values ap-guangzhou \
    --Filters.0.MatchType Equals \
    --Tags.0.Key 部门 \
    --Tags.0.Value 开发部
```

Output: 
```
{
    "Response": {
        "RequestId": "76b37805-f705-4907-8deb-36abae09e4ed"
    }
}
```

