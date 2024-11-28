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
                "NodeId": 101,
                "ParentNodeId": 0,
                "Remark": "",
                "UpdateTime": "2021-04-16 11:49:39"
            }
        ],
        "RequestId": "becff4cb-fe62-4288-ac6c-4fba115b94b3",
        "Total": 1
    }
}
```

