**Example 1: 查询任务详情**



Input: 

```
tccli ciam ListJobs --cli-unfold-argument  \
    --UserStoreId 2c3aca3b****************a7efe88e \
    --JobIds c29f2c0f****************405ec698
```

Output: 
```
{
    "Response": {
        "JobSet": [
            {
                "Id": "c29f2c0f****************405ec698",
                "Status": "PENDING",
                "Type": "IMPORT_USER",
                "CreatedDate": 1715156770024,
                "Format": "NDJSON",
                "Location": "http://aa.com/bb.csv",
                "ErrorDetails": [
                    {
                        "UserId": "53e25c3****************e4eb5bd1",
                        "Error": "error message"
                    }
                ],
                "FailedUsers": [
                    {
                        "FailedUserIdentification": "53e25c3****************e4eb5bd1",
                        "FailedReason": "error reason"
                    }
                ]
            }
        ],
        "RequestId": "e2e9e8aa********************9ab34c6e"
    }
}
```

