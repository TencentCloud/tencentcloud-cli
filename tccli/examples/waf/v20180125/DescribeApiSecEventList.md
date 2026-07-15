**Example 1: api安全事件列表**



Input: 

```
tccli waf DescribeApiSecEventList --cli-unfold-argument  \
    --Domain qcloudwaf.com
```

Output: 
```
{
    "Response": {
        "RequestId": "cd63d5b2-9d4e-46db-8cfd-b1c448cc8e47",
        "Data": [
            {
                "EventId": "api_asfa",
                "EventType": "",
                "Domain": "hzh.qcloud.com",
                "Mode": "1",
                "StartTime": 0,
                "UpdateTime": 0,
                "ApiName": "/api",
                "Level": "400",
                "Method": ""
            }
        ],
        "Total": 213
    }
}
```

