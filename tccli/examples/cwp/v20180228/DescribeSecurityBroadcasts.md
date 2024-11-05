**Example 1: 安全播报列表页**



Input: 

```
tccli cwp DescribeSecurityBroadcasts --cli-unfold-argument  \
    --EndDate 2019-11-25 \
    --BeginDate 2019-12-25 \
    --Limit 1 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "List": [
            {
                "Subtitle": "安全播报",
                "Level": 1,
                "Title": "安全播报",
                "CreateTime": "2019-12-25 11:57:15",
                "Type": 1,
                "Id": 1
            }
        ],
        "RequestId": "5b49dea4-0d0e-400f-8d11-2fdf1707c51a "
    }
}
```

