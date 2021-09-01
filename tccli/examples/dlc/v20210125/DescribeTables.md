**Example 1: 示例1**

查询数据表列表。

Input: 

```
tccli dlc DescribeTables --cli-unfold-argument  \
    --Limit 1 \
    --Offset 0 \
    --DatabaseName database-test
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "TableList": [
            {
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
            }
        ],
        "RequestId": "xx"
    }
}
```

