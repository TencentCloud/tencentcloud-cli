**Example 1: 查询边缘节点**

查询指定分组的边缘节点

Input: 

```
tccli ioa DescribeDLPEdgeNodes --cli-unfold-argument  \
    --Condition.PageNum 1 \
    --Condition.PageSize 10 \
    --Condition.Filters.0.Field GroupId \
    --Condition.Filters.0.Operator eq \
    --Condition.Filters.0.Values ioa_default_group_id \
    --Condition.Sort.Field UTime \
    --Condition.Sort.Order desc
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "EdgeNodeId": "d2hi48v7sdjjc675mpc0",
                    "EdgeNodeName": "深圳节点3",
                    "GroupId": "d2hhpaf7sdjjc675mp5g",
                    "GroupName": "深圳节点",
                    "Id": 6,
                    "Ip": "1.1.1.3"
                },
                {
                    "EdgeNodeId": "d2hi47f7sdjjc675mpbg",
                    "EdgeNodeName": "深圳节点2",
                    "GroupId": "d2hhpaf7sdjjc675mp5g",
                    "GroupName": "深圳节点",
                    "Id": 5,
                    "Ip": "1.1.1.2"
                }
            ],
            "Page": {
                "PageCount": 1,
                "PageNum": 1,
                "PageSize": 10,
                "Total": 5
            }
        },
        "RequestId": "e853fda5-34fb-42e2-8c72-b8bbcc9e8906"
    }
}
```

