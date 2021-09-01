**Example 1: 查询单元化规则列表**



Input: 

```
tccli tsf DescribeUnitRules --cli-unfold-argument  \
    --GatewayInstanceId gw-ins-afsfas \
    --Offset 0 \
    --Limit 20 \
    --SearchWord xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "efa09114-e0c3-43ec-8347-5f4454696c61",
        "Result": {
            "TotalCount": 1,
            "Content": [
                {
                    "Id": "gw-xxxxxxx",
                    "GatewayInstanceId": "test",
                    "Name": null,
                    "Status": "enabled"
                }
            ]
        }
    }
}
```

