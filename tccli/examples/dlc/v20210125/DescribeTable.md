**Example 1: 示例1**



Input: 

```
tccli dlc DescribeTable --cli-unfold-argument  \
    --DatabaseName database-test \
    --TableName table-test
```

Output: 
```
{
    "Response": {
        "Table": {
            "InputFormat": "xx",
            "ModifiedTime": "xx",
            "TableBaseInfo": {
                "TableName": "xx",
                "DatabaseName": "xx"
            },
            "CreateTime": "xx",
            "Location": "xx",
            "Properties": [
                {
                    "Value": "xx",
                    "Key": "xx"
                }
            ],
            "Columns": [
                {
                    "Comment": "xx",
                    "Type": "xx",
                    "Name": "xx"
                }
            ],
            "Partitions": [
                {
                    "Comment": "xx",
                    "Type": "xx",
                    "Name": "xx"
                }
            ]
        },
        "RequestId": "xx"
    }
}
```

