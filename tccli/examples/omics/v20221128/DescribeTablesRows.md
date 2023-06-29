**Example 1: 查询表格行数据**

查询表格行数据。

Input: 

```
tccli omics DescribeTablesRows --cli-unfold-argument  \
    --ProjectId prj-aggressive-lime-porcupine-752427 \
    --TableId tab-cold-purple-barnacle-251091 \
    --Offset 0 \
    --Limit 10 \
    --Filters.0.Name Tr \
    --Filters.0.Values .txt \
    --Filters.1.Name TableRowUuid \
    --Filters.1.Values d3154292-9305-42cb-99ab-a0fc1f5112ac 41363765-71e4-42ad-bbf8-bed9e70cd85e
```

Output: 
```
{
    "Response": {
        "RequestId": "288e5644-82c2-445f-b852-198bd6242b0c",
        "Rows": [
            {
                "Content": [
                    "10",
                    "cos://gene-1252949230/batch_base_test/input/10.txt"
                ],
                "TableRowUuid": "41363765-71e4-42ad-bbf8-bed9e70cd85e"
            },
            {
                "Content": [
                    "11",
                    "cos://gene-1252949230/batch_base_test/input/11.txt"
                ],
                "TableRowUuid": "d3154292-9305-42cb-99ab-a0fc1f5112ac"
            }
        ],
        "TotalCount": 2
    }
}
```

