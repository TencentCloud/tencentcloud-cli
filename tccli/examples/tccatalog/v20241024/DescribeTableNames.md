**Example 1: 列出asy_dlc 下面的list_test下所有表**



Input: 

```
tccli tccatalog DescribeTableNames --cli-unfold-argument  \
    --CatalogName asy_dlc \
    --SchemaName list_test
```

Output: 
```
{
    "Response": {
        "RequestId": "3701dda3-0a78-4157-8c10-55d24ae7de27",
        "TableNames": [
            {
                "Name": "tbl_34",
                "Namespace": [
                    "default",
                    "asy_dlc",
                    "list_test"
                ]
            },
            {
                "Name": "tbl_33",
                "Namespace": [
                    "default",
                    "asy_dlc",
                    "list_test"
                ]
            },
            {
                "Name": "tbl_32",
                "Namespace": [
                    "default",
                    "asy_dlc",
                    "list_test"
                ]
            },
            {
                "Name": "tbl_31",
                "Namespace": [
                    "default",
                    "asy_dlc",
                    "list_test"
                ]
            },
            {
                "Name": "hive_5",
                "Namespace": [
                    "default",
                    "asy_dlc",
                    "list_test"
                ]
            },
            {
                "Name": "hive_4",
                "Namespace": [
                    "default",
                    "asy_dlc",
                    "list_test"
                ]
            },
            {
                "Name": "hive_3",
                "Namespace": [
                    "default",
                    "asy_dlc",
                    "list_test"
                ]
            },
            {
                "Name": "hive_2",
                "Namespace": [
                    "default",
                    "asy_dlc",
                    "list_test"
                ]
            },
            {
                "Name": "hive_1",
                "Namespace": [
                    "default",
                    "asy_dlc",
                    "list_test"
                ]
            },
            {
                "Name": "tbl_24",
                "Namespace": [
                    "default",
                    "asy_dlc",
                    "list_test"
                ]
            },
            {
                "Name": "tbl_23",
                "Namespace": [
                    "default",
                    "asy_dlc",
                    "list_test"
                ]
            },
            {
                "Name": "tbl_22",
                "Namespace": [
                    "default",
                    "asy_dlc",
                    "list_test"
                ]
            },
            {
                "Name": "tbl_21",
                "Namespace": [
                    "default",
                    "asy_dlc",
                    "list_test"
                ]
            },
            {
                "Name": "tbl_15",
                "Namespace": [
                    "default",
                    "asy_dlc",
                    "list_test"
                ]
            },
            {
                "Name": "tbl_14",
                "Namespace": [
                    "default",
                    "asy_dlc",
                    "list_test"
                ]
            },
            {
                "Name": "tbl_13",
                "Namespace": [
                    "default",
                    "asy_dlc",
                    "list_test"
                ]
            },
            {
                "Name": "tbl_12",
                "Namespace": [
                    "default",
                    "asy_dlc",
                    "list_test"
                ]
            },
            {
                "Name": "tbl_11",
                "Namespace": [
                    "default",
                    "asy_dlc",
                    "list_test"
                ]
            },
            {
                "Name": "tbl_5",
                "Namespace": [
                    "default",
                    "asy_dlc",
                    "list_test"
                ]
            },
            {
                "Name": "tbl_4",
                "Namespace": [
                    "default",
                    "asy_dlc",
                    "list_test"
                ]
            },
            {
                "Name": "tbl_3",
                "Namespace": [
                    "default",
                    "asy_dlc",
                    "list_test"
                ]
            },
            {
                "Name": "tbl_2",
                "Namespace": [
                    "default",
                    "asy_dlc",
                    "list_test"
                ]
            },
            {
                "Name": "tbl_1",
                "Namespace": [
                    "default",
                    "asy_dlc",
                    "list_test"
                ]
            }
        ]
    }
}
```

