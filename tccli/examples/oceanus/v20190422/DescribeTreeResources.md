**Example 1: 查询指定依赖**

查询指定依赖

Input: 

```
tccli oceanus DescribeTreeResources --cli-unfold-argument  \
    --Filters.0.Name ResourceName \
    --Filters.0.Values normal \
    --WorkSpaceId space-53rqk422
```

Output: 
```
{
    "Response": {
        "Children": null,
        "Id": "root",
        "Items": [
            {
                "FileName": "1317959670/deep_normal_flink-hello-world-1.0.0.jar",
                "FolderId": "root",
                "Name": "1317959670/deep_normal_flink-hello-world-1.0.0.jar",
                "RefJobStatusCountSet": [],
                "Remark": "deep normal size",
                "ResourceId": "resource-er9pkk0o",
                "ResourceType": 1
            },
            {
                "FileName": "normal_flink-hello-world-1.0.0.jar",
                "FolderId": "root",
                "Name": "normal_flink-hello-world-1.0.0.jar",
                "RefJobStatusCountSet": [],
                "Remark": "normal size",
                "ResourceId": "resource-jvwtg594",
                "ResourceType": 1
            }
        ],
        "Name": "依赖目录",
        "ParentId": "",
        "RequestId": "78d06002-44d2-46fa-8f63-14f51b0237d3",
        "TotalCount": 2
    }
}
```

**Example 2: 分类中的自定义树状结构并筛选**

用户点击作业管理页面中的分类的自定义树状结构并点击分类旁的筛选按钮选择作业类型

Input: 

```
tccli oceanus DescribeTreeResources --cli-unfold-argument  \
    --Filters.0.Name ResourceName \
    --Filters.0.Values 111
```

Output: 
```
{
    "Response": {
        "Children": [
            {
                "ParentId": "root",
                "Id": "folder-xxxxx",
                "Name": "folder-name",
                "Items": null,
                "Children": null,
                "TotalCount": 0
            }
        ],
        "Id": "root",
        "Items": [
            {
                "ResourceId": "resource-xxxxxx",
                "Name": "flink-connector-jdbc.jar",
                "ResourceType": 1,
                "Remark": "pgsql1",
                "FileName": "flink-connector-jdbc.jar",
                "FolderId": "root",
                "RefJobStatusCountSet": [
                    {
                        "JobStatus": 5,
                        "Count": 2
                    }
                ]
            }
        ],
        "Name": "依赖目录",
        "ParentId": "",
        "RequestId": "4aafc302-4fc5-44f5-9e90-2e0a2702ab81",
        "TotalCount": 333
    }
}
```

