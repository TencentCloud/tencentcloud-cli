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
        "Data": {
            "Count": 1,
            "List": [
                {
                    "NameListId": 33,
                    "ListName": "手机黑名单",
                    "ListType": 1,
                    "DataType": 2,
                    "Status": 1,
                    "Remark": "remark",
                    "CreateTime": "2020-06-19 18:23:25",
                    "UpdateTime": "2020-06-19 18:23:25",
                    "EffectCount": "7/8",
                    "SceneCode": "all_scene"
                }
            ]
        },
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

