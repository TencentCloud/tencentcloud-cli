**Example 1: 查询vpc通道绑定api列表**



Input: 

```
tccli apigateway DescribeUpstreamBindApis --cli-unfold-argument  \
    --UpstreamId “upstream-0c96l2bo” \
    --Limit 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Result": {
            "TotalCount": 1,
            "BindApiSet": [
                {
                    "ApiId": "xx",
                    "ServiceName": "xx",
                    "BindTime": "2020-09-22T00:00:00+00:00",
                    "ApiName": "xx",
                    "ServiceId": "xx"
                }
            ]
        },
        "RequestId": "xx"
    }
}
```

