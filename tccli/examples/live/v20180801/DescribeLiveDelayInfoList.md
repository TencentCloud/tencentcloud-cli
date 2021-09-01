**Example 1: 请求示例**



Input: 

```
tccli live DescribeLiveDelayInfoList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "DelayInfoList": [
            {
                "DomainName": "5000.pushdomain.com",
                "AppName": "live",
                "StreamName": "testStream",
                "DelayInterval": 60,
                "CreateTime": "2019-06-14T00:00:00Z",
                "ExpireTime": "2019-06-15T00:00:00Z",
                "Status": 1
            }
        ],
        "RequestId": "8e50cdb5-56dc-408b-89b0-31818958d424"
    }
}
```

