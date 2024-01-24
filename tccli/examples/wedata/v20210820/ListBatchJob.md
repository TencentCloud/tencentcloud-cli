**Example 1: 示例**



Input: 

```
tccli wedata ListBatchJob --cli-unfold-argument  \
    --ProjectId abc \
    --JobType abc \
    --OwnerId abc \
    --StartOperateTime abc \
    --EndOperateTime abc \
    --Page 0 \
    --Size 0 \
    --SortType abc \
    --SortItem abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "TotalCount": 0,
            "TotalPage": 0,
            "PageCount": 0,
            "PageSize": 0,
            "Items": [
                {
                    "JobId": 0,
                    "JobType": "abc",
                    "Status": "abc",
                    "CreateTime": "abc",
                    "OwnerName": "abc",
                    "ProjectId": "abc"
                }
            ],
            "PageNumber": 0
        },
        "RequestId": "abc"
    }
}
```

