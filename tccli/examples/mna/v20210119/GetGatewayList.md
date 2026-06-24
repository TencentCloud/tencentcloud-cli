**Example 1: 示例1**



Input: 

```
tccli mna GetGatewayList --cli-unfold-argument  \
    --GatewayName abc \
    --PageNumber 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "GatewayList": [
            {
                "GatewayId": "abc",
                "GatewayName": "abc",
                "CreateTime": 1709191947,
                "Status": 1
            }
        ],
        "Total": 1,
        "RequestId": "abc"
    }
}
```

