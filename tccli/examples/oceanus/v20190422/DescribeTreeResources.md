**Example 1: 分类中的自定义树状结构并筛选**

用户点击作业管理页面中的分类的自定义树状结构并点击分类旁的筛选按钮选择作业类型

Input: 

```
tccli oceanus DescribeTreeResources --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "ParentId": "xx",
        "Id": "xx",
        "Name": "xx",
        "Items": [
            {
                "ResourceId": "xx",
                "Name": "xx",
                "ResourceType": 0,
                "Remark": "xx",
                "FileName": "xx",
                "FolderId": "xx"
            }
        ],
        "Children": [
            {
                "ParentId": "xx",
                "Id": "xx",
                "Name": "xx",
                "Items": [
                    {
                        "ResourceId": "xx",
                        "Name": "xx",
                        "ResourceType": 0,
                        "Remark": "xx",
                        "FileName": "xx",
                        "FolderId": "xx"
                    }
                ],
                "Children": [
                    {
                        "ParentId": "xx",
                        "Id": "xx",
                        "Name": "xx",
                        "Items": [
                            {
                                "ResourceId": "xx",
                                "Name": "xx",
                                "ResourceType": 0,
                                "Remark": "xx",
                                "FileName": "xx",
                                "FolderId": "xx"
                            }
                        ],
                        "Children": [
                            {
                                "ParentId": "xx",
                                "Id": "xx",
                                "Name": "xx",
                                "TotalCount": 0
                            }
                        ],
                        "TotalCount": 0
                    }
                ],
                "TotalCount": 0
            }
        ],
        "TotalCount": 0,
        "RequestId": "xx"
    }
}
```

