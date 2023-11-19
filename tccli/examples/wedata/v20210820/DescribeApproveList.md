**Example 1: 成功示例**



Input: 

```
tccli wedata DescribeApproveList --cli-unfold-argument  \
    --ApproveClassification db \
    --PageNumber 0 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "RequestId": "f026f974-be6b-4856-a7d2-f4c8e12af81f",
        "Data": {
            "Rows": [
                {
                    "ApproveId": "1",
                    "ApplicantId": "100022741403",
                    "ApplicantName": "TBDS",
                    "Reason": "测试申请",
                    "Remark": null,
                    "Status": "new",
                    "ApproveType": "db_db",
                    "ApproveTypeName": "库申请",
                    "ApproveClassification": "db",
                    "ApproveClassificationName": "库表申请",
                    "CreateTime": "2022-02-18T11:30:09+08:00",
                    "ApproveTime": null
                }
            ],
            "PageNumber": 0,
            "PageSize": 10,
            "TotalCount": 1,
            "TotalPageNumber": 0
        }
    }
}
```

**Example 2: 成功示例2**



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
        "RequestId": "036e7eb9-578d-4271-bc1b-c9c016077b28",
        "Data": {
            "Rows": [
                {
                    "ApproveId": "38532",
                    "ApplicantId": "100015777150",
                    "ApplicantName": "三雨",
                    "Reason": "产品体验",
                    "Remark": null,
                    "Status": "new",
                    "ApproveType": "db_table",
                    "ApproveTypeName": "表申请",
                    "ApproveClassification": "db",
                    "ApproveClassificationName": "库表申请",
                    "CreateTime": "2022-03-08T13:10:21+08:00",
                    "ApproveTime": null
                },
                {
                    "ApproveId": "38531",
                    "ApplicantId": "100022256608",
                    "ApplicantName": "fe",
                    "Reason": "大是大非",
                    "Remark": null,
                    "Status": "new",
                    "ApproveType": "db_db",
                    "ApproveTypeName": "库申请",
                    "ApproveClassification": "db",
                    "ApproveClassificationName": "库表申请",
                    "CreateTime": "2022-03-08T11:54:28+08:00",
                    "ApproveTime": null
                },
                {
                    "ApproveId": "38530",
                    "ApplicantId": "100022256608",
                    "ApplicantName": "fe",
                    "Reason": "让我",
                    "Remark": null,
                    "Status": "new",
                    "ApproveType": "db_table",
                    "ApproveTypeName": "表申请",
                    "ApproveClassification": "db",
                    "ApproveClassificationName": "库表申请",
                    "CreateTime": "2022-03-08T11:50:07+08:00",
                    "ApproveTime": null
                },
                {
                    "ApproveId": "38529",
                    "ApplicantId": "100022256608",
                    "ApplicantName": "fe",
                    "Reason": "123",
                    "Remark": null,
                    "Status": "new",
                    "ApproveType": "db_table",
                    "ApproveTypeName": "表申请",
                    "ApproveClassification": "db",
                    "ApproveClassificationName": "库表申请",
                    "CreateTime": "2022-03-08T10:39:04+08:00",
                    "ApproveTime": null
                },
                {
                    "ApproveId": "38528",
                    "ApplicantId": "100015777150",
                    "ApplicantName": "三雨",
                    "Reason": "产品体验",
                    "Remark": null,
                    "Status": "new",
                    "ApproveType": "db_table",
                    "ApproveTypeName": "表申请",
                    "ApproveClassification": "db",
                    "ApproveClassificationName": "库表申请",
                    "CreateTime": "2022-03-08T10:35:06+08:00",
                    "ApproveTime": null
                },
                {
                    "ApproveId": "38527",
                    "ApplicantId": "100022187615",
                    "ApplicantName": "jonsljiang",
                    "Reason": "%22%2526r1%3Dxsscallback%2523%22",
                    "Remark": null,
                    "Status": "new",
                    "ApproveType": "db_table",
                    "ApproveTypeName": "表申请",
                    "ApproveClassification": "db",
                    "ApproveClassificationName": "库表申请",
                    "CreateTime": "2022-03-08T02:14:03+08:00",
                    "ApproveTime": null
                },
                {
                    "ApproveId": "38526",
                    "ApplicantId": "100022187615",
                    "ApplicantName": "jonsljiang",
                    "Reason": "%22%2526callback%3Dxsscallback%2523%22",
                    "Remark": null,
                    "Status": "new",
                    "ApproveType": "db_table",
                    "ApproveTypeName": "表申请",
                    "ApproveClassification": "db",
                    "ApproveClassificationName": "库表申请",
                    "CreateTime": "2022-03-08T02:14:00+08:00",
                    "ApproveTime": null
                },
                {
                    "ApproveId": "38525",
                    "ApplicantId": "100022187615",
                    "ApplicantName": "jonsljiang",
                    "Reason": "测试",
                    "Remark": null,
                    "Status": "new",
                    "ApproveType": "db_table",
                    "ApproveTypeName": "表申请",
                    "ApproveClassification": "db",
                    "ApproveClassificationName": "库表申请",
                    "CreateTime": "2022-03-08T02:14:00+08:00",
                    "ApproveTime": null
                },
                {
                    "ApproveId": "38524",
                    "ApplicantId": "100022187615",
                    "ApplicantName": "jonsljiang",
                    "Reason": "测试",
                    "Remark": null,
                    "Status": "new",
                    "ApproveType": "db_table",
                    "ApproveTypeName": "表申请",
                    "ApproveClassification": "db",
                    "ApproveClassificationName": "库表申请",
                    "CreateTime": "2022-03-08T02:13:59+08:00",
                    "ApproveTime": null
                },
                {
                    "ApproveId": "38523",
                    "ApplicantId": "100022187615",
                    "ApplicantName": "jonsljiang",
                    "Reason": "测试",
                    "Remark": null,
                    "Status": "new",
                    "ApproveType": "db_table",
                    "ApproveTypeName": "表申请",
                    "ApproveClassification": "db",
                    "ApproveClassificationName": "库表申请",
                    "CreateTime": "2022-03-08T02:13:56+08:00",
                    "ApproveTime": null
                }
            ],
            "PageNumber": 0,
            "PageSize": 10,
            "TotalCount": 21493,
            "TotalPageNumber": 2149
        }
    }
}
```

