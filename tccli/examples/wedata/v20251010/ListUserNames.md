**Example 1: demo**



Input: 

```
tccli wedata ListUserNames --cli-unfold-argument  \
    --PageRequest.PageNumber 1 \
    --PageRequest.PageSize 3
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "Uin": "7064618",
                    "UserName": "wedata"
                },
                {
                    "Uin": "720187",
                    "UserName": "tsinghu"
                },
                {
                    "Uin": "7006734",
                    "UserName": "mem"
                }
            ],
            "PageResponse": {
                "PageNumber": 1,
                "PageSize": 3,
                "TotalCount": 16,
                "TotalPageNumber": 6
            }
        },
        "RequestId": "0284279c-b7fc-4882-992e-d8bc606a1a49"
    }
}
```

