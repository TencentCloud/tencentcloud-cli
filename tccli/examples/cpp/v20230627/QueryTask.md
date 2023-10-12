**Example 1: QueryTask**



Input: 

```
tccli cpp QueryTask --cli-unfold-argument  \
    --WorkId abc \
    --Offset 0 \
    --Limit 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "Results": [
                {
                    "InfringeId": 0,
                    "Author": "abc",
                    "AuthorId": "abc",
                    "CrawlTime": "abc",
                    "Duration": "abc",
                    "InfringeTitle": "abc",
                    "WorkName": "abc",
                    "PlatformName": "abc",
                    "PlayNum": "abc",
                    "PublishTime": "abc",
                    "ReceiveTime": "abc",
                    "TaskId": "abc",
                    "Url": "abc",
                    "WorkId": "abc",
                    "MediaType": 0,
                    "Similarity": 0,
                    "ExtraInfo": {
                        "IpCompany": "abc",
                        "IpPubtime": "abc",
                        "IpScene": "abc"
                    }
                }
            ],
            "Offset": 0,
            "Sum": 0
        },
        "RequestId": "abc"
    }
}
```

