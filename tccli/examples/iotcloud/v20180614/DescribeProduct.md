**Example 1: 查看产品详情示例**



Input: 

```
tccli iotcloud DescribeProduct --cli-unfold-argument  \
    --ProductId ABCDE12345
```

Output: 
```
{
    "Response": {
        "ProductMetadata": {
            "CreationDate": 1509453755000
        },
        "ProductProperties": {
            "ProductDescription": "description1"
        },
        "ProductName": "Test_1",
        "ProductId": "ABCDE12345",
        "RequestId": "8e0b3665-cfb5-4077-a535-0ed7f970cf3b"
    }
}
```

