**Example 1: 查询CRM统计数据接口**



Input: 

```
tccli wav QueryCrmStatistics --cli-unfold-argument  \
    --SalesId xx \
    --Cursor xx \
    --Limit 0 \
    --BeginTime 1 \
    --OrgId 1 \
    --EndTime 1
```

Output: 
```
{
    "Response": {
        "NextCursor": "+1H24tK0tELjSiTOR10DzA==",
        "PageData": [
            {
                "LeadCnt": 0,
                "BuildCnt": 0,
                "InvitedCnt": 0,
                "OrderedCnt": 0,
                "DeliveredCnt": 0,
                "DefeatCnt": 0,
                "NewContactCnt": 0,
                "StatisticalTime": "String"
            }
        ],
        "RequestId": "b1a024bf-4d74-4b5d-a5bd-bbec330520e8"
    }
}
```

