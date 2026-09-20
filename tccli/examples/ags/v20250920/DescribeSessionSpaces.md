**Example 1: 分页查询会话空间**

查询当前应用及地域下的会话空间列表，每页返回 20 条数据。

Input: 

```
tccli ags DescribeSessionSpaces --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "SessionSpaces": [
            {
                "CreateTime": "2026-08-17T03:51:17.608Z",
                "Default": false,
                "Description": "Reserved for sessions generated during a seasonal marketing campaign.",
                "Name": "Seasonal Campaign Temporary Space",
                "SpaceId": "space-22eed49f-e3ae-4b4a-8efa-4cd961bf4764",
                "Status": "Active",
                "UpdateTime": "2026-08-17T03:51:17.608Z"
            }
        ],
        "TotalCount": 3,
        "RequestId": "9d08f066-c47e-4e5d-ae9c-a51d7edf01a6"
    }
}
```

**Example 2: 按描述筛选会话空间**

使用 description-like 筛选描述中包含“DSH Brain Session cookbook”的会话空间，返回匹配的空间列表及总数。

Input: 

```
tccli ags DescribeSessionSpaces --cli-unfold-argument  \
    --Filters.0.Name description-like \
    --Filters.0.Values 'DSH Brain Session cookbook'
```

Output: 
```
{
    "Response": {
        "SessionSpaces": [
            {
                "CreateTime": "2026-09-03T08:03:05.279Z",
                "Default": false,
                "Description": "DSH Brain Session cookbook Chongqing validation",
                "Name": "dsh-session-cq-09031603",
                "SpaceId": "space-04664885-bd66-4a51-83f5-5f6132f8642a",
                "Status": "Active",
                "UpdateTime": "2026-09-03T08:03:05.279Z"
            }
        ],
        "TotalCount": 1,
        "RequestId": "de553d46-8094-4644-a68b-ed6b3db7b07c"
    }
}
```

