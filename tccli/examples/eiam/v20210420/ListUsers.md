**Example 1: 请求示例**



Input: 

```
tccli eiam ListUsers --cli-unfold-argument  \
    --SearchCondition.Keyword "" \
    --ExpectedFields UserId UserName DisplayName LastUpdateTime Status \
    --Sort.SortKey LastUpdateTime \
    --Sort.SortOrder ASC \
    --Limit 2 \
    --Offset 0 \
    --IncludeTotal True
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "RequestId": "2151788c-****-47be-8a6f-5ca114fcfbeb",
        "UserList": []
    }
}
```

