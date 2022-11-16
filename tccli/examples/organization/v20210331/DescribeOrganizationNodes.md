**Example 1: 获取节点列表**



Input: 

```
tccli organization DescribeOrganizationNodes --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "CreateTime": "2021-04-16 11:49:39",
                "Name": "Root",
                "NodeId": 26,
                "ParentNodeId": 0,
                "Remark": "",
                "UpdateTime": "2021-04-16 11:49:39"
            },
            {
                "CreateTime": "2021-04-16 14:59:57",
                "Name": "test",
                "NodeId": 27,
                "ParentNodeId": 26,
                "Remark": "test",
                "UpdateTime": "2021-04-16 14:59:57"
            },
            {
                "CreateTime": "2021-04-16 15:55:53",
                "Name": "test1",
                "NodeId": 29,
                "ParentNodeId": 27,
                "Remark": "1",
                "UpdateTime": "2021-04-16 15:55:53"
            }
        ],
        "RequestId": "becff4cb-fe62-4288-ac6c-4fba115b94b3",
        "Total": 3
    }
}
```

