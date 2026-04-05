**Example 1: demo**

demo

Input: 

```
tccli wedata ListConsoleGroups --cli-unfold-argument  \
    --PageRequest.PageNumber 1 \
    --PageRequest.PageSize 23
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "CreateTime": "1761371099",
                    "GroupId": "17613710998352474",
                    "GroupName": "test1024",
                    "Roles": [],
                    "UpdateTime": "1761371099",
                    "UserCount": 0
                },
                {
                    "CreateTime": "1761375145",
                    "GroupId": "17613751452682686",
                    "GroupName": "test1025",
                    "Roles": [],
                    "UpdateTime": "1761375145",
                    "UserCount": 0
                },
                {
                    "CreateTime": "1761375642",
                    "GroupId": "17613756425238050",
                    "GroupName": "test1020_1",
                    "Roles": [],
                    "UpdateTime": "1761375642",
                    "UserCount": 0
                },
                {
                    "CreateTime": "1761748910",
                    "GroupId": "17617489100805200",
                    "GroupName": "test1",
                    "Roles": [],
                    "UpdateTime": "1761748910",
                    "UserCount": 0
                },
                {
                    "CreateTime": "1761837772",
                    "GroupId": "17618377721112568",
                    "GroupName": "abel1030",
                    "Roles": [],
                    "UpdateTime": "1761837772",
                    "UserCount": 0
                },
                {
                    "CreateTime": "1761902344",
                    "GroupId": "17619023441437512",
                    "GroupName": "abel1031",
                    "Roles": [],
                    "UpdateTime": "1761902344",
                    "UserCount": 0
                }
            ],
            "PageResponse": {
                "PageNumber": 1,
                "PageSize": 23,
                "TotalCount": 6,
                "TotalPageNumber": 1
            }
        },
        "RequestId": "101bf651-30eb-4a56-848c-88c199539bef"
    }
}
```

