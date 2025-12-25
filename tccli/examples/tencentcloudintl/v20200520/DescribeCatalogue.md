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
                            "Children": [
                                {
                                    "CategoryId": 213,
                                    "Children": [],
                                    "DocType": "default",
                                    "Extension": "",
                                    "FirstReleaseTime": "2016-07-04 00:00:00",
                                    "Id": 4939,
                                    "Lang": "en",
                                    "PdfUrl": "https://staticintl.cloudcachetci.com/doc/pdf/test/product/pdf/213_4939_en.pdf",
                                    "Pid": 2277,
                                    "RecentReleaseTime": "2016-07-04 00:00:00",
                                    "Title": "Instance Overview",
                                    "Type": "page",
                                    "Weight": 100
                                }
                            ],
                            "DocType": "default",
                            "Extension": "",
                            "FirstReleaseTime": "2019-01-01 00:00:00",
                            "Id": 2277,
                            "Lang": "en",
                            "PdfUrl": "",
                            "Pid": 492,
                            "RecentReleaseTime": "2019-01-01 00:00:00",
                            "Title": "Instance",
                            "Type": "directory",
                            "Weight": 80
                        }
                    ],
                    "DocType": "default",
                    "Extension": "",
                    "FirstReleaseTime": "2019-01-01 00:00:00",
                    "Id": 492,
                    "Lang": "en",
                    "PdfUrl": "https://staticintl.cloudcachetci.com/doc/pdf/test/product/pdf/213_492_en.pdf",
                    "Pid": 0,
                    "RecentReleaseTime": "2019-01-01 00:00:00",
                    "Title": "Product Introduction",
                    "Type": "directory",
                    "Weight": 100
                }
            ],
            "OverviewPageConfig": "{\"key\":\"val\"}",
            "Title": "Microservice and Serverless Microservice and Serverless"
        },
        "RequestId": "ac71d226-b3d0-40d9-bcb7-2e3a2048f9d3"
    }
}
```

