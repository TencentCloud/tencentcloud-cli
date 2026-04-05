**Example 1: 获取模型名称列表**

获取模型名称列表

Input: 

```
tccli wedata ListModelNames --cli-unfold-argument  \
    --CatalogName yb_test05 \
    --SchemaName sc_test05 \
    --MaxResults 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "Name": "MyPredictiveModel",
                    "Namespace": [
                        "yb_test05",
                        "sc_test05"
                    ]
                }
            ],
            "NextPageToken": "eyJsaW1pdCI6MSwib2Zmc2V0IjoxfQ==",
            "TotalCount": "51"
        },
        "RequestId": "17d320c2-bceb-45e6-8634-28289ffd71c7"
    }
}
```

