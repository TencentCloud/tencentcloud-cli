**Example 1: 获取MySQL表结构**



Input: 

```
tccli wedata GetTableSchemaInfo --cli-unfold-argument  \
    --Name t_chat_custom_knowledge \
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
            "Schemas": [
                {
                    "ColumnKey": "",
                    "Comment": "主键ID",
                    "Name": "id",
                    "Type": "bigint(20)"
                }
            ]
        },
        "RequestId": "88304c39-0cd4-4c6c-804c-8434b176aa1b"
    }
}
```

