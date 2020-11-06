**Example 1: Getting figure sample list**



Input: 

```
tccli vod DescribePersonSamples --cli-unfold-argument  \
    --PersonIds 10569 \
    --Names 'John Smith' \
    --Tags Celebrity \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "PersonSet": [
            {
                "PersonId": "10569",
                "Name": "John Smith",
                "Description": "Chinese actor, director, and producer",
                "FaceInfoSet": [
                    {
                        "FaceId": "10024",
                        "Url": "http://1256768367.vod2.myqcloud.com/8b0dd2b5vodcq1256768367/4d27b39f5285890783754292994/face.jpeg"
                    }
                ],
                "TagSet": [
                    "U.S.",
                    "Celebrity"
                ],
                "CreateTime": "2018-10-01T10:00:00Z",
                "UpdateTime": "2018-10-01T10:00:00Z"
            }
        ],
        "RequestId": "7d80775f-fb6d-4204-9540-1876f0d1c5a9"
    }
}
```

