**Example 1: 查询MySQL表数据**



Input: 

```
tccli wedata ListTablesPage --cli-unfold-argument  \
    --DatabaseName application_chatbi \
    --ConnectionType MySQL \
    --WorkspaceId 17663856806379896 \
    --ConnectionId dc03eaf1-7f9b-4128-8c18-68ec95187d08
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "TableName": "t_chat_custom_knowledge"
                }
            ],
            "NextPageToken": "eyJsaW1pdCI6MTAsIm9mZnNldCI6MTB9"
        },
        "RequestId": "4e7ef570-8bee-4ebb-aacf-f8e1268b03fb"
    }
}
```

**Example 2: 查询TCLake Volume**



Input: 

```
tccli wedata ListTablesPage --cli-unfold-argument  \
    --DatabaseName newvolume \
    --ConnectionType TCLake \
    --WorkspaceId 17663856806379896 \
    --SchemaName schema_01 \
    --MaxResults 100 \
    --SubType Volume
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "TableName": "11"
                }
            ],
            "NextPageToken": ""
        },
        "RequestId": "69e29602-6569-40cc-8296-3462286f2c90"
    }
}
```

