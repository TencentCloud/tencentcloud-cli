**Example 1: 1**



Input: 

```
tccli databuddy ListTableNames --cli-unfold-argument  \
    --CatalogName lsj_test \
    --SchemaName default \
    --WorkspaceId 17678671667189298 \
    --MaxResults 10 \
    --CatalogSource METALAKE
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "CatalogSource": "METALAKE",
                    "Name": "wen_shu_idc__shu_ju_yang_li",
                    "Namespace": [
                        "lsj_test"
                    ],
                    "Status": "0"
                }
            ],
            "NextPageToken": "eyJvZmZzZXQiOjEwfQ=="
        },
        "RequestId": "117797e6-c0ed-495c-bdcc-31a014857a0f"
    }
}
```

