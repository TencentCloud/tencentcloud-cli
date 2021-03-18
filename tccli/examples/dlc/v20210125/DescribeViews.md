**Example 1: 示例1**

查询数据表列表。

Input: 

```
tccli dlc DescribeViews --cli-unfold-argument  \
    --Limit 1 \
    --Offset 0 \
    --DatabaseName database-test
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "xx",
        "ViewList": [
            {
                "ModifiedTime": "xx",
                "ViewBaseInfo": {
                    "ViewName": "xx",
                    "DatabaseName": "xx"
                },
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
                "CreateTime": "xx"
            }
        ]
    }
}
```

