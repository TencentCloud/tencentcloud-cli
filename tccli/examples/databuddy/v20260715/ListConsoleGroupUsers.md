**Example 1: 示例1**



Input: 

```
tccli databuddy ListConsoleGroupUsers --cli-unfold-argument  \
    --GroupId 17848631472347483 \
    --UserUins 700002576299 \
    --PageNumber 1 \
    --PageSize 11
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "CreateTime": "1784863675",
                    "Nickname": "junzha",
                    "UpdateTime": "1784863675",
                    "UserName": "junzha",
                    "UserUin": "700002576299"
                }
            ],
            "PageNumber": 1,
            "PageSize": 11,
            "TotalCount": 1,
            "TotalPageNumber": 1
        },
        "RequestId": "a5ad1add-0b88-4882-ac8e-3afb7bc569fc"
    }
}
```

