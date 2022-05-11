**Example 1: 查询产品资源详情**



Input: 

```
tccli iotcloud DescribeProductResource --cli-unfold-argument  \
    --ProductID ABCDE12345 \
    --Name test
```

Output: 
```
{
    "Response": {
        "Result": {
            "Name": "xx",
            "ProductName": "xx",
            "Md5": "xx",
            "Description": "xx",
            "ProductID": "xx",
            "CreateTime": "xx",
            "Size": 1
        },
        "RequestId": "xx"
    }
}
```

