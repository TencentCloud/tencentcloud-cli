**Example 1: 查询任务详情**



Input: 

```
tccli ciam ListJobs --cli-unfold-argument  \
    --UserStoreId xx \
    --JobIds xx
```

Output: 
```
{
    "Response": {
        "JobSet": [
            {
                "Status": "xx",
                "Format": "xx",
                "FailedUsers": [
                    {
                        "FailedUserIdentification": "xx",
                        "FailedReason": "xx"
                    }
                ],
                "Location": "xx",
                "Type": "xx",
                "Id": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

