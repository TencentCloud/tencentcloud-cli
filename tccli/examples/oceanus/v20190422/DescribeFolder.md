**Example 1: 查询文件夹**

查询文件夹

Input: 

```
tccli oceanus DescribeFolder --cli-unfold-argument  \
    --FolderId folder-bnjsm2sb \
    --WorkSpaceId space-7rfcnslf \
    --FolderType 1
```

Output: 
```
{
    "Response": {
        "FolderId": "folder-bnjsm2sb",
        "FolderName": "6.9_connector",
        "FolderType": 1,
        "ParentId": "root",
        "RequestId": "3ca249e8-b742-4e97-856d-1fca5a95d6a5",
        "SubFolderInfo": [
            {
                "FolderId": "folder-gbtcphg0",
                "FolderName": "hive_catalog_config_311"
            },
            {
                "FolderId": "folder-79b2dxuc",
                "FolderName": "sql_server"
            },
            {
                "FolderId": "folder-oc406jen",
                "FolderName": "doris"
            },
            {
                "FolderId": "folder-3ldo2w3g",
                "FolderName": "mysql_cdc"
            },
            {
                "FolderId": "folder-nodi86tq",
                "FolderName": "kudu"
            }
        ],
        "WorkSpaceId": "space-7rfcnslf"
    }
}
```

