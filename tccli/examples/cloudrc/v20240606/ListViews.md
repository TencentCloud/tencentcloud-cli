**Example 1: 按viewId列表查询视图**



Input: 

```
tccli cloudrc ListViews --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0 \
    --Filters.0.Name viewId \
    --Filters.0.Values vw-dlrk6v8u vw-sihwx8yh
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Tags": [
                    {
                        "Key": "部门",
                        "Value": "开发部"
                    },
                    {
                        "Key": "应用",
                        "Value": "默认应用"
                    }
                ],
                "ViewCreateTime": "2024-12-23 17:54:00",
                "ViewId": "vw-dlrk6v8u",
                "ViewName": "后付费资源视图",
                "ViewUpdateTime": "2024-12-23 17:54:00"
            },
            {
                "Tags": [
                    {
                        "Key": "部门",
                        "Value": "开发部"
                    }
                ],
                "ViewCreateTime": "2024-12-23 17:53:30",
                "ViewId": "vw-sihwx8yh",
                "ViewName": "广州地域视图",
                "ViewUpdateTime": "2024-12-23 17:53:30"
            }
        ],
        "RequestId": "2a8fda9e-5cb0-420b-9f53-323d9650e22b",
        "TotalCount": 2
    }
}
```

**Example 2: 按标签查询视图**



Input: 

```
tccli cloudrc ListViews --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0 \
    --Filters.0.Name tag:部门 \
    --Filters.0.Values 开发部 质量部
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Tags": [
                    {
                        "Key": "部门",
                        "Value": "开发部"
                    },
                    {
                        "Key": "应用",
                        "Value": "默认应用"
                    }
                ],
                "ViewCreateTime": "2024-12-23 17:54:00",
                "ViewId": "vw-dlrk6v8u",
                "ViewName": "后付费资源视图",
                "ViewUpdateTime": "2024-12-23 17:54:00"
            },
            {
                "Tags": [
                    {
                        "Key": "部门",
                        "Value": "开发部"
                    }
                ],
                "ViewCreateTime": "2024-12-23 17:53:30",
                "ViewId": "vw-sihwx8yh",
                "ViewName": "广州地域视图",
                "ViewUpdateTime": "2024-12-23 17:53:30"
            },
            {
                "Tags": [
                    {
                        "Key": "部门",
                        "Value": "开发部"
                    }
                ],
                "ViewCreateTime": "2024-12-23 17:52:42",
                "ViewId": "vw-5kk86nm4",
                "ViewName": "开发部视图",
                "ViewUpdateTime": "2024-12-23 17:52:42"
            }
        ],
        "RequestId": "a4d664d0-bceb-48dc-aa4b-11c5ff48e116",
        "TotalCount": 3
    }
}
```

**Example 3: 按标签键“且”视图名称模糊匹配查询视图**



Input: 

```
tccli cloudrc ListViews --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0 \
    --Filters.0.Name tagKey \
    --Filters.0.Values 部门 \
    --Filters.1.Name viewName \
    --Filters.1.Values 视图
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Tags": [
                    {
                        "Key": "部门",
                        "Value": "开发部"
                    },
                    {
                        "Key": "应用",
                        "Value": "默认应用"
                    }
                ],
                "ViewCreateTime": "2024-12-23 17:54:00",
                "ViewId": "vw-dlrk6v8u",
                "ViewName": "后付费资源视图",
                "ViewUpdateTime": "2024-12-23 17:54:00"
            },
            {
                "Tags": [
                    {
                        "Key": "部门",
                        "Value": "开发部"
                    }
                ],
                "ViewCreateTime": "2024-12-23 17:53:30",
                "ViewId": "vw-sihwx8yh",
                "ViewName": "广州地域视图",
                "ViewUpdateTime": "2024-12-23 17:53:30"
            },
            {
                "Tags": [
                    {
                        "Key": "部门",
                        "Value": "开发部"
                    }
                ],
                "ViewCreateTime": "2024-12-23 17:52:42",
                "ViewId": "vw-5kk86nm4",
                "ViewName": "开发部视图",
                "ViewUpdateTime": "2024-12-23 17:52:42"
            }
        ],
        "RequestId": "f435875e-fe33-4c6d-9869-e3c4fc8086f9",
        "TotalCount": 3
    }
}
```

**Example 4: 查询前10个视图**



Input: 

```
tccli cloudrc ListViews --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Tags": [
                    {
                        "Key": "部门",
                        "Value": "开发部"
                    },
                    {
                        "Key": "应用",
                        "Value": "默认应用"
                    }
                ],
                "ViewCreateTime": "2024-12-23 17:54:00",
                "ViewId": "vw-dlrk6v8u",
                "ViewName": "后付费资源视图",
                "ViewUpdateTime": "2024-12-23 17:54:00"
            },
            {
                "Tags": [
                    {
                        "Key": "部门",
                        "Value": "开发部"
                    }
                ],
                "ViewCreateTime": "2024-12-23 17:53:30",
                "ViewId": "vw-sihwx8yh",
                "ViewName": "广州地域视图",
                "ViewUpdateTime": "2024-12-23 17:53:30"
            },
            {
                "Tags": [
                    {
                        "Key": "应用",
                        "Value": "默认应用"
                    }
                ],
                "ViewCreateTime": "2024-12-23 17:53:01",
                "ViewId": "vw-6frh7g3i",
                "ViewName": "默认应用视图",
                "ViewUpdateTime": "2024-12-23 17:53:01"
            },
            {
                "Tags": [
                    {
                        "Key": "部门",
                        "Value": "开发部"
                    }
                ],
                "ViewCreateTime": "2024-12-23 17:52:42",
                "ViewId": "vw-5kk86nm4",
                "ViewName": "开发部视图",
                "ViewUpdateTime": "2024-12-23 17:52:42"
            }
        ],
        "RequestId": "21ea0a7c-b2f9-4e54-bf12-5231dd23d663",
        "TotalCount": 4
    }
}
```

