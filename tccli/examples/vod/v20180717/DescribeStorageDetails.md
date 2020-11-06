**Example 1: Querying VOD storage usage statistics**

This example shows you how to query the storage capacity usage between December 1, 2018 (inclusive) and December 7, 2018 (inclusive).

Input: 

```
tccli vod DescribeStorageDetails --cli-unfold-argument  \
    --StartTime 2018-12-01T00:00:00+08:00 \
    --EndTime 2018-12-07T00:00:00+08:00
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Time": "2018-12-01T00:00:00+08:00",
                "Value": 1000000
            },
            {
                "Time": "2018-12-02T00:00:00+08:00",
                "Value": 1500000
            },
            {
                "Time": "2018-12-03T00:00:00+08:00",
                "Value": 1500000
            },
            {
                "Time": "2018-12-04T00:00:00+08:00",
                "Value": 1500000
            },
            {
                "Time": "2018-12-05T00:00:00+08:00",
                "Value": 1500000
            },
            {
                "Time": "2018-12-06T00:00:00+08:00",
                "Value": 1500000
            },
            {
                "Time": "2018-12-07T00:00:00+08:00",
                "Value": 1500000
            }
        ],
        "RequestId": "requestId"
    }
}
```

