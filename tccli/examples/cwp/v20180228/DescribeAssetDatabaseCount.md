**Example 1: 获取所有数据库数量**



Input: 

```
tccli cwp DescribeAssetDatabaseCount --cli-unfold-argument  \
    --Name host1
```

Output: 
```
{
    "Response": {
        "Databases": [
            {
                "Key": "mysql",
                "Value": 1,
                "Desc": "mysql 5.7",
                "NewCount": 0
            }
        ],
        "RequestId": "07a92740-5e54-4ea6-9320-c6fc3f3a1121"
    }
}
```

