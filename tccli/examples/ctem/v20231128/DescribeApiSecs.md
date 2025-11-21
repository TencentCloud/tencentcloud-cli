**Example 1: 查看API安全数据**



Input: 

```
tccli ctem DescribeApiSecs --cli-unfold-argument  \
    --Filters.0.Name IsRiskAPI \
    --Filters.0.Values 1 \
    --CustomerId 100275
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Code": 200,
                "DisplayToolCommon": {
                    "CreateAt": "2025-08-11 16:32:20",
                    "CustomerId": 100275,
                    "CustomerName": "腾讯测试",
                    "Detail": "",
                    "EnterpriseName": "",
                    "EnterpriseUid": "",
                    "Ignored": false,
                    "JobId": 0,
                    "JobRecordId": 0,
                    "JobStageId": 0,
                    "Labels": "{}",
                    "Md5": "55e3de2116082d108358d1dbf3fbe4c4",
                    "UpdateAt": "2025-08-11 16:33:40"
                },
                "Host": "http://test.com",
                "Id": 1006,
                "IsRiskAPI": true,
                "Method": "POST",
                "Path": "/v1/api",
                "Request": "",
                "Response": "",
                "Status": "",
                "Url": "http://test.com/v1/api"
            }
        ],
        "RequestId": "302c99a9-5449-424d-b116-061a63977200",
        "Total": 1
    }
}
```

