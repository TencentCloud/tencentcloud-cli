**Example 1: ModifyNameListData**



Input: 

```
tccli rce ModifyNameListData --cli-unfold-argument  \
    --BusinessSecurityData.DataList.0.Status 1 \
    --BusinessSecurityData.DataList.0.Remark "测试" \
    --BusinessSecurityData.DataList.0.DataContent "xxx.xx.12.123" \
    --BusinessSecurityData.DataList.0.NameListDataId 73 \
    --BusinessSecurityData.DataList.0.StartTime '"2020-03-02 20:50:00"' \
    --BusinessSecurityData.DataList.0.EndTime '"2020-03-02 20:50:00"'
```

Output: 
```
{
    "Response": {
        "Data": {
            "Code": 0,
            "Message": "OK",
            "Value": []
        },
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

