**Example 1: 获取模型版本列表**

获取模型版本列表

Input: 

```
tccli wedata ListModelVersions --cli-unfold-argument  \
    --CatalogName yb_test05 \
    --SchemaName sc_test05 \
    --ModelName randyrren1 \
    --MaxResults 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [],
            "NextPageToken": "",
            "TotalCount": "0"
        },
        "RequestId": "6dbfbd25-09fb-4277-8fa3-a91fffa99d48"
    }
}
```

