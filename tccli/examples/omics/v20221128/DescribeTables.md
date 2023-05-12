**Example 1: 查询表格**

查询表格。

Input: 

```
tccli omics DescribeTables --cli-unfold-argument  \
    --ProjectId prj-aggressive-lime-porcupine-752427 \
    --Filters.0.Name Name \
    --Filters.0.Values test \
    --Filters.1.Name TableId \
    --Filters.1.Values tab-cold-purple-barnacle-251091
```

Output: 
```
{
    "Response": {
        "RequestId": "8baa213d-e5c5-4e38-a3a4-562e71b5210b",
        "Tables": [
            {
                "Columns": [
                    {
                        "DataType": "String",
                        "Header": "runId"
                    },
                    {
                        "DataType": "File",
                        "Header": "fileName"
                    }
                ],
                "CreateTime": "2023-03-16 16:44:24",
                "Creator": "100029430413",
                "Description": "cloudapi_test",
                "Name": "cloudapi_test_1",
                "ProjectId": "prj-aggressive-lime-porcupine-752427",
                "TableId": "tab-cold-purple-barnacle-251091"
            }
        ],
        "TotalCount": 1
    }
}
```

