**Example 1: 获取位置空间列表**



Input: 

```
tccli iotexplorer GetPositionSpaceList --cli-unfold-argument  \
    --ProjectId prj-projectid \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "List": [
            {
                "UpdateTime": 1598863974,
                "Description": "desc",
                "ProjectId": "prj",
                "AuthorizeType": 0,
                "SpaceId": "id",
                "ProductIdList": [
                    "ProductId"
                ],
                "CreateTime": 1598863974,
                "SpaceName": "name",
                "Icon": "icon",
                "Zoom": 0
            }
        ],
        "RequestId": "xx"
    }
}
```

