**Example 1: 查询TCLake Volume**



Input: 

```
tccli wedata ListDatabasesPage --cli-unfold-argument  \
    --ConnectionType TCLAKE \
    --WorkspaceId 17663856806379896 \
    --SubType Volume
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "DatabaseName": "newvolume"
                }
            ],
            "NextPageToken": ""
        },
        "RequestId": "b0ceb493-2542-470d-b22c-ed05ee1d3729"
    }
}
```

