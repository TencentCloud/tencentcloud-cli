**Example 1: demo**



Input: 

```
tccli wedata ListConsoleAddableUsers --cli-unfold-argument  \
    --PageRequest.PageNumber 1 \
    --PageRequest.PageSize 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "Nickname": "wedata30",
                    "Uin": "7064618",
                    "UserName": "wedata30"
                }
            ],
            "PageResponse": {
                "PageNumber": 1,
                "PageSize": 1,
                "TotalCount": 16,
                "TotalPageNumber": 16
            }
        },
        "RequestId": "d602f35c-f09a-4895-a01f-955eb14f6e73"
    }
}
```

