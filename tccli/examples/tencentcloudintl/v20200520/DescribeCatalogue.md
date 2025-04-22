**Example 1: 获取213分类数据**



Input: 

```
tccli tencentcloudintl DescribeCatalogue --cli-unfold-argument  \
    --CategoryId 213 \
    --Lang en
```

Output: 
```
{
    "Response": {
        "Data": {
            "Lang": "en",
            "List": [
                {
                    "CategoryId": 213,
                    "Children": [
                        {
                            "CategoryId": 213,
                            "Children": [],
                            "DocType": "default",
                            "Extension": "",
                            "FirstReleaseTime": "2016-09-06 00:00:00",
                            "Id": 6091,
                            "Lang": "en",
                            "PdfUrl": "",
                            "Pid": 492,
                            "RecentReleaseTime": "2016-09-06 00:00:00",
                            "Title": "Regions and Availability Zones",
                            "Type": "page",
                            "Weight": 95
                        }
                    ],
                    "Title": "Microservice and Serverless Microservice and Serverless"
                }
            ]
        },
        "RequestId": "034711f0-99d7-4524-b1fb-2241c1e92094"
    }
}
```

