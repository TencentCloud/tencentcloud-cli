**Example 1: 查看软件详情列表**



Input: 

```
tccli ioa DescribeSoftwareInformation --cli-unfold-argument  \
    --Mid 123
```

Output: 
```
{
    "Response": {
        "RequestId": "ada4c0d5-2e2d-4264-93b9-c067a4ddb62e",
        "Data": {
            "Items": [],
            "Page": {
                "Total": 0,
                "PageCount": 0,
                "PageSize": 1000,
                "PageNum": 1
            }
        }
    }
}
```

**Example 2: 1**

~

Input: 

```
tccli ioa DescribeSoftwareInformation --cli-unfold-argument  \
    --Mid abc \
    --Condition.Filters.0.Field abc \
    --Condition.Filters.0.Operator abc \
    --Condition.Filters.0.Values abc \
    --Condition.FilterGroups.0.Filters.0.Field abc \
    --Condition.FilterGroups.0.Filters.0.Operator abc \
    --Condition.FilterGroups.0.Filters.0.Values abc \
    --Condition.Sort.Field abc \
    --Condition.Sort.Order abc \
    --Condition.PageSize 0 \
    --Condition.PageNum 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "Name": "abc",
                    "InstallDate": "abc",
                    "SoftwareId": 0,
                    "Mid": "abc",
                    "Version": "abc",
                    "CorpName": "abc",
                    "Id": 0,
                    "PiracyRisk": 0
                }
            ],
            "Page": {
                "PageSize": 1,
                "PageNum": 1,
                "PageCount": 1,
                "Total": 1
            }
        },
        "RequestId": "abc"
    }
}
```

