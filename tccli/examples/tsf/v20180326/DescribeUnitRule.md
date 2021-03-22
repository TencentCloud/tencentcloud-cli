**Example 1: 查询单元化规则详情**



Input: 

```
tccli tsf DescribeUnitRule --cli-unfold-argument  \
    --Id gw-ins-afsfas
```

Output: 
```
{
    "Response": {
        "RequestId": "efa09114-e0c3-43ec-8347-5f4454696c61",
        "Result": {
            "Id": "rule-xxxxxxx",
            "GatewayInstanceId": "test",
            "Name": null,
            "Status": "enabled"
        }
    }
}
```

