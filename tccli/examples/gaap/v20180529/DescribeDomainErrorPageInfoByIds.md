**Example 1: DescribeDomainErrorPageInfoByIds**



Input: 

```
tccli gaap DescribeDomainErrorPageInfoByIds --cli-unfold-argument  \
    --ErrorPageIds errorPage-lhlnux1v
```

Output: 
```
{
    "Response": {
        "RequestId": "8d9f4d84-b825-4a4f-8c4c-3c87c559c84c",
        "ErrorPageSet": [
            {
                "Body": "sx",
                "Status": 0,
                "Domain": "test.domain",
                "ClearHeaders": [
                    "MyClearHeader",
                    "MyClearHeader1"
                ],
                "ListenerId": "listener-23egjhxb",
                "ErrorNos": [
                    501,
                    502
                ],
                "ErrorPageId": "errorPage-lhlnux1v",
                "NewErrorNo": 4123,
                "SetHeaders": [
                    {
                        "HeaderName": "MyName",
                        "HeaderValue": "MyValue"
                    },
                    {
                        "HeaderName": "MyName1",
                        "HeaderValue": "MyValue1"
                    }
                ]
            }
        ]
    }
}
```

