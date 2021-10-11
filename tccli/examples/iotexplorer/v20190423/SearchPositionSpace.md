**Example 1: SearchPositionSpace**



Input: 

```
tccli iotexplorer SearchPositionSpace --cli-unfold-argument  \
    --ProjectId prj-projectid \
    --SpaceName name \
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

