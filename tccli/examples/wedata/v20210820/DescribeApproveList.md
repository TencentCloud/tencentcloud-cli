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
        "Data": {
            "Rows": [
                {
                    "ApplicantId": "abc",
                    "ApplicantName": "abc",
                    "Remark": "abc",
                    "ApproveClassification": "abc",
                    "ApproveId": "abc",
                    "ApproveType": "abc",
                    "Reason": "abc",
                    "CreateTime": "abc",
                    "ApproveTime": "abc",
                    "ApproveClassificationName": "abc",
                    "Status": "abc",
                    "ApproveTypeName": "abc",
                    "ErrorMessage": "abc",
                    "ApplyName": "abc",
                    "ApproverId": "abc",
                    "ApproverName": "abc"
                }
            ],
            "TotalPageNumber": 1,
            "TotalCount": 1,
            "PageNumber": 1,
            "PageSize": 1
        },
        "RequestId": "abc"
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
        "Data": {
            "Rows": [
                {
                    "ApplicantId": "abc",
                    "ApplicantName": "abc",
                    "Remark": "abc",
                    "ApproveClassification": "abc",
                    "ApproveId": "abc",
                    "ApproveType": "abc",
                    "Reason": "abc",
                    "CreateTime": "abc",
                    "ApproveTime": "abc",
                    "ApproveClassificationName": "abc",
                    "Status": "abc",
                    "ApproveTypeName": "abc",
                    "ErrorMessage": "abc",
                    "ApplyName": "abc",
                    "ApproverId": "abc",
                    "ApproverName": "abc"
                }
            ],
            "TotalPageNumber": 1,
            "TotalCount": 1,
            "PageNumber": 1,
            "PageSize": 1
        },
        "RequestId": "abc"
    }
}
```

