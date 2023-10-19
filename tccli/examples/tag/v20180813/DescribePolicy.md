**Example 1: 获取标签策略**

获取标签策略

Input: 

```
tccli tag DescribePolicy --cli-unfold-argument  \
    --PolicyId 10004
```

Output: 
```
{
    "Response": {
        "PolicyId": 10004,
        "Name": "地域标签",
        "Description": "地域标签",
        "Content": "{\"tags\":{\"Region\":{\"tag_key\":{\"@@assign\":\"Region\"},\"tag_value\":{\"@@assign\":[\"ap-guangzhou\"]}}}}",
        "RequestId": "b53af52d-082f-4b74-b7da-310b41c78ade"
    }
}
```

