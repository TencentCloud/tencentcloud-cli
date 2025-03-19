**Example 1: 获取产品资源列表**



Input: 

```
tccli iotcloud DescribeProductResources --cli-unfold-argument  \
    --ProductID EQPOKD5111 \
    --Offset 0 \
    --Limit 10 \
    --Name myname
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Result": [
            {
                "Name": "myname",
                "ProductName": "dev-001",
                "Md5": "EQPOKD5111",
                "Description": "mydescription",
                "ProductID": "",
                "CreateTime": "2021-04-20 12:07:28",
                "Size": 1
            }
        ],
        "RequestId": "ebea2fd8-0b8f-44b3-99ab-1b04fcfb6cbd"
    }
}
```

