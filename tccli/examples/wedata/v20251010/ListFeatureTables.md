**Example 1: 特征表列表**

特征表列表

Input: 

```
tccli wedata ListFeatureTables --cli-unfold-argument  \
    --WorkspaceId 17678671667189298 \
    --MaxResults 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "AssetGuid": "",
                    "Comment": "",
                    "CreateTime": "1770108951108",
                    "DatabaseName": "ericpuwang_test",
                    "FullName": "DataLakeCatalog.ericpuwang_test.lyw_wine_0203_v3",
                    "ModifiedTime": "1770108951732",
                    "Name": "lyw_wine_0203_v3",
                    "Tags": [],
                    "WorkspaceId": ""
                }
            ],
            "NextPageToken": "eyJzZWFyY2hBZnRlclZhbHVlcyI6WzIuMTgyMzIxNSwidGNjYXRhbG9nLnYxLnVpZDExNzYyMDc5NTMyMzI5NjAzMzhAMjYwMDczNDkzX2FwLWd1YW5nemhvdV9UQUJMRSJdfQ==",
            "TotalCount": "0"
        },
        "RequestId": "772c43cd-449e-4d5e-81f4-5f6ca61cb0fb"
    }
}
```

