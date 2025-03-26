**Example 1: 查询产品资源详情**



Input: 

```
tccli iotcloud DescribeProductResource --cli-unfold-argument  \
    --ProductID EQPOKD5111 \
    --Name myname
```

Output: 
```
{
    "Response": {
        "Result": {
            "Name": "myname",
            "ProductName": "dev-001",
            "Md5": "EQPOefdgad1",
            "Description": "mydescription",
            "ProductID": "EQPOKD5111",
            "CreateTime": "2021-04-20 12:07:28",
            "Size": 1
        },
        "RequestId": "ebea2fd8-0b8f-44b3-99ab-1b04fcfb6cbc"
    }
}
```

