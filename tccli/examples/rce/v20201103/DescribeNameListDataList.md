**Example 1: DescribeNameListDataList**



Input: 

```
tccli rce DescribeNameListDataList --cli-unfold-argument  \
    --BusinessSecurityData.NameListId 33 \
    --BusinessSecurityData.Status 1 \
    --BusinessSecurityData.PageNumber 1 \
    --BusinessSecurityData.PageSize 10
```

Output: 
```
{
    "Response": {
        "Data": {},
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

