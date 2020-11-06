**Example 1: DescribeDomainErrorPageInfo**



Input: 

```
tccli gaap DescribeDomainErrorPageInfo --cli-unfold-argument  \
    --ListenerId 0 \
    --Domain a.com
```

Output: 
```
{
    "Response": {
        "RequestId": "8d9f4d84-b825-4a4f-8c4c-3c87c559c84c",
        "ErrorPageSet": [
            {
                "Body": null,
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
                "NewErrorNo": null,
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

