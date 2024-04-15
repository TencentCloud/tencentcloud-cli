**Example 1: 成功示例2**



Input: 

```
tccli wedata DescribeApproveList --cli-unfold-argument  \
    --OrderFields.0.Direction DESC \
    --OrderFields.0.Name CreateTime \
    --ApproveClassification db \
    --PageNumber 0 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "Data": {
            "Rows": [
                {
                    "ApplicantId": "1000297561131",
                    "ApplicantName": "test_0",
                    "ApplyName": "test_db1520729990156341",
                    "ApproveClassification": "db",
                    "ApproveClassificationName": "库表申请",
                    "ApproveId": "23133",
                    "ApproveProjectName": "project_test",
                    "ApproveTime": "2022-04-11T07:06:16+08:00",
                    "ApproveType": "db_db",
                    "ApproveTypeName": "库申请",
                    "ApproverId": "100408890356",
                    "ApproverName": "EST",
                    "CreateTime": "2022-04-12T06:15:16+08:00",
                    "ErrorMessage": "null",
                    "Reason": "use test",
                    "Remark": "test",
                    "Status": "reject"
                }
            ],
            "TotalPageNumber": 1,
            "TotalCount": 1,
            "PageNumber": 1,
            "PageSize": 1
        },
        "RequestId": "ef5f33da-4f24-41b0-bc89-979bd6737625"
    }
}
```

