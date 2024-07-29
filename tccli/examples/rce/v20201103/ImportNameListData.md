**Example 1: ImportNameListData**



Input: 

```
tccli rce ImportNameListData --cli-unfold-argument  \
    --BusinessSecurityData.NameListId 33 \
    --BusinessSecurityData.DataSource 2 \
    --BusinessSecurityData.DataContentInfo.0.DataContent "xxx.xx.0.1";
```

Output: 
```
{
    "Response": {
        "Data": {
            "Message": "OK",
            "Code": 0,
            "Value": []
        },
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

