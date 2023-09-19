**Example 1: 示例**



Input: 

```
tccli cwp DescribeSecurityBroadcasts --cli-unfold-argument  \
    --EndDate xx \
    --BeginDate xx \
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
                "Subtitle": "xx",
                "Level": 1,
                "Title": "xx",
                "CreateTime": "xx",
                "Type": 1,
                "Id": 1
            }
        ],
        "RequestId": "5b49dea4-0d0e-400f-8d11-2fdf1707c51a "
    }
}
```

