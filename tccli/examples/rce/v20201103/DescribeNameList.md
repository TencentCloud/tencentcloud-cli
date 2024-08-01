**Example 1: DescribeNameList**



Input: 

```
tccli rce DescribeNameList --cli-unfold-argument  \
    --BusinessSecurityData.Status 1 \
    --BusinessSecurityData.DataType 1 \
    --BusinessSecurityData.ListType 1 \
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

