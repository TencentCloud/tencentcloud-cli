**Example 1: 请求示例**

获取某个账号下的所有导播台列表

Input: 

```
tccli live DescribeCasterList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03",
        "CasterList": [
            {
                "CasterId": 10,
                "CasterName": "example",
                "StartBillingTime": 0,
                "StopBillingTime": 1731964027,
                "Description": "",
                "CreateTime": 1603158528,
                "Status": 0,
                "ExpireTime": -1,
                "FeeType": 0
            }
        ]
    }
}
```

