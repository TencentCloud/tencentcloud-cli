**Example 1: 请求示例**



Input: 

```
tccli live DescribeLiveForbidStreamList --cli-unfold-argument  \
    --PageNum 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "ForbidStreamList": [
            {
                "StreamName": "5000_abcdefg",
                "CreateTime": "2019-01-16T12:00:00Z",
                "ExpireTime": "2019-04-16T12:00:00Z"
            }
        ],
        "TotalNum": 1,
        "TotalPage": 1,
        "PageNum": 1,
        "PageSize": 10,
        "RequestId": "8e50cdb5-56dc-408b-89b0-31818958d424"
    }
}
```

