**Example 1: 分类中的自定义树状结构并筛选**

用户点击作业管理页面中的分类的自定义树状结构并点击分类旁的筛选按钮选择作业类型

Input: 

```
tccli oceanus DescribeTreeJobs --cli-unfold-argument  \
    --Filters.0.Name JobType \
    --Filters.0.Values 1 2
```

Output: 
```
{
    "Response": {
        "Children": [
            {
                "ParentId": "root",
                "Id": "folder-xxx",
                "Name": "test",
                "JobSet": [
                    {
                        "JobId": "cql-xxxx",
                        "Name": "test_xxxx",
                        "JobType": 1,
                        "RunningCu": 0,
                        "Status": 5
                    },
                    {
                        "JobId": "cql-xxxx",
                        "Name": "test_xxxx",
                        "JobType": 1,
                        "RunningCu": 0,
                        "Status": 5
                    }
                ],
                "Children": null,
                "RequestId": "015e7c7e-dad7-4bdb-9a16-b348ef8c1457"
            }
        ],
        "Id": "root",
        "JobSet": [],
        "Name": "作业列表",
        "ParentId": "",
        "RequestId": "015e7c7e-dad7-4bdb-9a16-b348ef8c1457"
    }
}
```

