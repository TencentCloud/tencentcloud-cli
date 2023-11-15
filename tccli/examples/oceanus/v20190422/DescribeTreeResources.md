**Example 1: 分类中的自定义树状结构并筛选**

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

