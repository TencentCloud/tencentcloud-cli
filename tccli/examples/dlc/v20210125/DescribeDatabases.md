**Example 1: 示例1**

查询数据库列表

Input: 

```
tccli dlc DescribeDatabases --cli-unfold-argument  \
    --Limit 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "xx",
        "DatabaseList": [
            {
                "Comment": "xx",
                "ModifiedTime": "xx",
                "Properties": [
                    {
                        "Value": "xx",
                        "Key": "xx"
                    }
                ],
                "DatabaseName": "xx",
                "CreateTime": "xx"
            }
        ]
    }
}
```

