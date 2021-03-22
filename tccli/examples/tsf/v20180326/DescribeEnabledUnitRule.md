**Example 1: 查询生效的单元化规则**



Input: 

```
tccli tsf DescribeEnabledUnitRule --cli-unfold-argument  \
    --GatewayInstanceId gw-ins-afsfas
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

