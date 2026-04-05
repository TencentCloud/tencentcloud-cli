**Example 1: demo**



Input: 

```
tccli wedata ListGroupUsers --cli-unfold-argument  \
    --GroupId 17613710998352474 \
    --PageRequest.PageNumber 1 \
    --PageRequest.PageSize 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [],
            "PageResponse": {
                "PageNumber": 1,
                "PageSize": 1,
                "TotalCount": 0,
                "TotalPageNumber": 0
            }
        },
        "RequestId": "4389c60c-e0f6-4080-be84-7d1e796a6f4c"
    }
}
```

