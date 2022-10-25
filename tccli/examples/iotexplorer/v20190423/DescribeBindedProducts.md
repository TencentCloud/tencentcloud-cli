**Example 1: 获取网关产品已经绑定的子产品**



Input: 

```
tccli iotexplorer DescribeBindedProducts --cli-unfold-argument  \
    --GatewayProductId ABCDE12345 \
    --ProductSource 0 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Products": [
            {
                "ProductId": "5SJN3W8XG6",
                "ProductName": "nhi7qhcp_StudioProduct101",
                "ProjectId": "5SJYTRW8XYT",
                "DataProtocol": 1,
                "DevStatus": "xx",
                "NetType": "xx",
                "ProductType": 0,
                "CategoryId": 0,
                "ProductOwnerName": "test"
            }
        ],
        "RequestId": "66245d34-a39b-41b5-85fa-8f8222c3e58e",
        "Total": 1
    }
}
```

