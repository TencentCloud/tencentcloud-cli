**Example 1: 查询绑定关系**



Input: 

```
tccli iotexplorer DescribeTWeTalkAgentBinding --cli-unfold-argument  \
    --ProductId M********6 \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Bindings": [
            {
                "AgentId": "agent-SValZ1qdEm",
                "BindingScope": "product",
                "CreateTime": 1781511871,
                "ProductId": "MD2JRU2IF6",
                "UpdateTime": 1781511871
            }
        ],
        "TotalCount": 3,
        "RequestId": "feb1aba0-a96d-4360-b6d6-f5edc89c9ffa"
    }
}
```

