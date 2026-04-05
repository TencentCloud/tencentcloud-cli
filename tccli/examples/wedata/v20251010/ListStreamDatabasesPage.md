**Example 1: 示例1**

示例1

Input: 

```
tccli wedata ListStreamDatabasesPage --cli-unfold-argument  \
    --MaxResults 1000 \
    --PageToken 1 \
    --ConnectionId 0108ec75-eafb-4294-95ce-78b55a1d2b61 \
    --ConnectionType MYSQL \
    --WorkspaceId 17663856806379896 \
    --Keyword 1 \
    --SubType 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "DatabaseName": "__cdb_recycle_bin__"
                }
            ],
            "NextPageToken": ""
        },
        "RequestId": "f083e507-6053-416b-a9c1-a4f2b5684bc5"
    }
}
```

