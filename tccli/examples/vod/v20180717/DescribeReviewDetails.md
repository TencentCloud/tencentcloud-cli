**Example 1: Querying VOD content audit duration statistics**



Input: 

```
tccli vod DescribeReviewDetails --cli-unfold-argument  \
    --StartTime 2018-12-01T16:00:00Z\
    --EndTime 2018-12-03T16:00:00Z
```

Output: 
```
{
    "Response": {
        "TotalCount": 10,
        "TotalDuration": 11901,
        "Data": [
            {
                "Time": "2018-12-01T16:00:00Z",
                "Value": 3600
            },
            {
                "Time": "2018-12-02T16:00:00Z",
                "Value": 4500
            },
            {
                "Time": "2018-12-03T16:00:00Z",
                "Value": 3801
            }
        ],
        "RequestId": "requestId"
    }
}
```

