**Example 1: 获取产品资源列表**



Input: 

```
tccli iotcloud DescribeProductResources --cli-unfold-argument  \
    --ProductID ABCDE12345 \
    --Offset 0 \
    --Limit 10 \
    --Name test
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Result": [
            {
                "Name": "xx",
                "ProductName": "xx",
                "Md5": "xx",
                "Description": "xx",
                "ProductID": "xx",
                "CreateTime": "xx",
                "Size": 1
            }
        ],
        "RequestId": "xx"
    }
}
```

