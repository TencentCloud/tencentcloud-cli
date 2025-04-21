**Example 1: DescribeSoftCategorySoftList**



Input: 

```
tccli ioa DescribeSoftCategorySoftList --cli-unfold-argument  \
    --OsType 0 \
    --AuthType 2 \
    --GroupId 40 \
    --Condition.Sort.Field Version \
    --Condition.Sort.Order desc \
    --CategoryId 7
```

Output: 
```
{
    "Response": {
        "RequestId": "ec485215-0b1d-49ad-b355-f718887d731c",
        "Data": {
            "Page": {
                "PageSize": 1000,
                "PageNum": 1,
                "PageCount": 0,
                "Total": 0
            },
            "SoftCategorySoftList": null,
            "Total": 0
        }
    }
}
```

