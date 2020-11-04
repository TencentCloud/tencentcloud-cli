**Example 1: 查询AttributeKey的有效取值范围**

查询AttributeKey的有效取值范围

Input: 

```
tccli cloudaudit GetAttributeKey --cli-unfold-argument  \
    --WebsiteType zh
```

Output: 
```
{
    "Response": {
        "RequestId": "6d833833-bbc6-4463-9a8f-6cc62d3a2afd",
        "AttributeKeyDetails": [
            {
                "Label": "只读",
                "Value": "ReadOnly",
                "Starter": "选择只读值",
                "LabelType": "select",
                "Order": 1
            },
            {
                "Label": "访问密钥",
                "Value": "AccessKeyId",
                "Starter": "输入访问密钥",
                "LabelType": "text",
                "Order": 2
            },
            {
                "Label": "请求ID",
                "Value": "RequestId",
                "Starter": "输入请求ID",
                "LabelType": "text",
                "Order": 3
            },
            {
                "Label": "事件名称",
                "Value": "EventName",
                "Starter": "选择事件名称",
                "LabelType": "select",
                "Order": 4
            },
            {
                "Label": "资源名称",
                "Value": "ResourceName",
                "Starter": "输入资源名称",
                "LabelType": "text",
                "Order": 5
            },
            {
                "Label": "资源类型",
                "Value": "ResourceType",
                "Starter": "选择资源类型",
                "LabelType": "select",
                "Order": 6
            },
            {
                "Label": "用户名称",
                "Value": "Username",
                "Starter": "选择用户名称",
                "LabelType": "select",
                "Order": 7
            }
        ]
    }
}
```

