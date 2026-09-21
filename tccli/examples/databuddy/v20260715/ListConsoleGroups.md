**Example 1: 示例1**



Input: 

```
tccli databuddy ListConsoleGroups --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 11 \
    --GroupKeyword bs_0630 \
    --GroupIds *****************
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "CreateTime": "1782790115",
                    "GroupId": "17827901155972706",
                    "GroupName": "bs_0630",
                    "GroupType": "1",
                    "Roles": [],
                    "UpdateTime": "1782790115",
                    "UserCount": 10
                }
            ],
            "PageNumber": 1,
            "PageSize": 11,
            "TotalCount": 1,
            "TotalPageNumber": 1
        },
        "RequestId": "93dc750e-41b5-4a56-b1ff-5019c4bf1d19"
    }
}
```

