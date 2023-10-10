**Example 1: 示例**



Input: 

```
tccli cwp CreateLogExport --cli-unfold-argument  \
    --Sort desc \
    --Count 500 \
    --Format json \
    --QueryString * \
    --StartTime 1656640800000 \
    --EndTime 1656641100000
```

Output: 
```
{
    "Response": {
        "ExportId": "export-dd7e975d-2ea0-4c3b-aad9-767c4beaafd5",
        "RequestId": "39715990-4996-447a-88c8-dc02034fb278"
    }
}
```

