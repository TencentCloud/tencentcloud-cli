**Example 1: 获取审批申请**



Input: 

```
tccli tcaplusdb DescribeApplications --cli-unfold-argument  \
    --TableGroupId xx \
    --ClusterId xx \
    --Applicant xx \
    --TableName xx \
    --Limit 1 \
    --Offset 1 \
    --CensorStatus 0 \
    --ApplyType 0
```

Output: 
```
{
    "Response": {
        "Applications": [
            {
                "Applicant": "100000012683",
                "ApplicationId": "4-169",
                "ApplicationStatus": 2,
                "ApplicationType": 2,
                "CanCensor": true,
                "CanWithdrawal": false,
                "ClusterId": "4",
                "ClusterName": "xml_1_ly",
                "CreatedTime": "2021-02-25 11:58:37",
                "ExecuteStatus": "-1",
                "ExecuteUser": "222",
                "TableGroupId": "1",
                "TableGroupName": "zone_1_1",
                "TableInstanceId": "null",
                "TableName": "add_table10",
                "TaskId": "0",
                "UpdateTime": "2021-02-25 11:58:37"
            }
        ],
        "RequestId": "fdsfdsfdsfdsf",
        "TotalCount": 92
    }
}
```

