**Example 1: DescribeImageAutoAuthorizedTaskList**



Input: 

```
tccli tcss DescribeImageAutoAuthorizedTaskList --cli-unfold-argument  \
    --StartTime 2022-01-01 \
    --EndTime 2022-01-07
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "List": [
            {
                "LastAuthorizedTime": "2020-09-22",
                "AuthorizedDate": "2020-09-22",
                "LatestFailCode": "REACH_LIMIT",
                "SuccessCount": 0,
                "FailCount": 0,
                "Source": "LOCAL",
                "TaskId": 1,
                "Type": "AUTO"
            }
        ],
        "RequestId": "8bc803fd-d85d-47b8-9e2b-9644674be677"
    }
}
```

