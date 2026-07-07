**Example 1: 创建负载均衡实例询价**



Input: 

```
tccli alb InquirePriceCreateLoadBalancer --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Price": {
            "InstancePrice": {
                "Discount": 100,
                "UnitPrice": 0.2,
                "UnitPriceDiscount": 0.2
            },
            "LcuPrice": {
                "Discount": 100,
                "UnitPrice": 0.049,
                "UnitPriceDiscount": 0.049
            }
        },
        "RequestId": "255917ce-96f9-46f6-9c13-8f498469e824"
    }
}
```

