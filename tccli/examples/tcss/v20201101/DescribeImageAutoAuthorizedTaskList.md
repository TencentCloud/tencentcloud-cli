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
                "LastAuthorizedTime": "xx",
                "AuthorizedDate": "2020-09-22",
                "LatestFailCode": "xx",
                "SuccessCount": 0,
                "FailCount": 0,
                "Source": "xx",
                "TaskId": 1,
                "Type": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

