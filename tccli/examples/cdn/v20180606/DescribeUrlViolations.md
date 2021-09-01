**Example 1: 违规历史查询**



Input: 

```
tccli cdn DescribeUrlViolations --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "ptplrss8qqf9x7534noql6",
        "UrlRecordList": [
            {
                "Id": 2256186,
                "RealUrl": "http://www.test.com/a.jpeg",
                "DownloadUrl": "2019-11-18/2019-11-18-18-26-08-1794844604-29-21-a.jpeg",
                "UrlStatus": "forbid",
                "CreateTime": "2019-11-17 18:25:47",
                "UpdateTime": "2019-11-18 18:06:47"
            }
        ],
        "TotalCount": 10
    }
}
```

