**Example 1: 根据事件ID查询资源栈事件详情**



Input: 

```
tccli tic DescribeStackEvents --cli-unfold-argument  \
    --EventIds ent-1armn3sg \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Events": [
            {
                "EventId": "ent-1armn3sg",
                "VersionId": "ver-kg8hn58h",
                "StackId": "stk-hz5vn3te",
                "Type": "plan",
                "Status": "success",
                "Message": "Message",
                "CreateTime": "2020-11-18T07:38:47.330Z"
            }
        ],
        "RequestId": "8ef5ccb0-4207-468b-bb07-a03e6a772caf"
    }
}
```

**Example 2: 根据事件类型，状态查询事件列表**



Input: 

```
tccli tic DescribeStackEvents --cli-unfold-argument  \
    --Filters.0.Name Type \
    --Filters.0.Values plan apply \
    --Filters.1.Name Status \
    --Filters.1.Values success \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "Events": [
            {
                "EventId": "ent-1armn3sg",
                "VersionId": "ver-kg8hn58h",
                "StackId": "stk-hz5vn3te",
                "Type": "plan",
                "Status": "success",
                "Message": "Message",
                "CreateTime": "2020-11-18T07:38:47.330Z"
            },
            {
                "EventId": "ent-1armn3sg",
                "VersionId": "ver-87bun57q",
                "StackId": "stk-ld7ln3sh",
                "Type": "apply",
                "Status": "success",
                "Message": "Message",
                "CreateTime": "2020-11-19T08:33:44.880Z"
            }
        ],
        "RequestId": "8ef5ccb0-4207-468b-bb07-a03e6a772caf"
    }
}
```

