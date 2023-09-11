**Example 1: 获取流程基础信息**

获取流程基础信息, 例子中查询2个合同流程的基础信息

Input: 

```
tccli ess DescribeFlowBriefs --cli-unfold-argument  \
    --Operator.UserId yDxVwUyKQWho8CUuO4zjEyQOAgwvr4Zy \
    --FlowIds yDRCLUUgygq2xun5UuO4zjEwg0vjoimj yDxbWUyKQDx7OZUuO4zjESvEkRMHc55R
```

Output: 
```
{
    "Response": {
        "RequestId": "s123456789",
        "FlowBriefs": [
            {
                "FlowId": "yDxbWUyKQDx7OZUuO4zjESvEkRMHc55R",
                "FlowName": "张三的入职合同",
                "FlowDescription": "张三10230822日入职需要签署的合同",
                "FlowType": "入职合同",
                "FlowStatus": 1,
                "CreatedOn": 1604910798,
                "FlowMessage": "",
                "Deadline": 1606910798,
                "Creator": "yDxbWUyKQDxPGGUuO4zjEyI4pZLqE2gh"
            },
            {
                "FlowId": "yDRCLUUgygq2xun5UuO4zjEwg0vjoimj",
                "FlowName": "采购1000台MacMini2合同",
                "FlowDescription": "8G256G配置电脑采购",
                "FlowType": "采购销售",
                "FlowStatus": 1,
                "CreatedOn": 1604910797,
                "FlowMessage": "",
                "Deadline": 1606910798,
                "Creator": "yDxVwUyKQWho8CUuO4zjEyQOAgwvr4Zy"
            }
        ]
    }
}
```

**Example 2: 获取流程基础信息失败情况**

获取流程基础信息, 但是没有对应合同流程的权限, 所以失败

Input: 

```
tccli ess DescribeFlowBriefs --cli-unfold-argument  \
    --Operator.UserId yDxVwUyKQWho8CUuO4zjEyQOAgwvr4Zy \
    --FlowIds yDwqYUZzwwjn1UEq1XhgvJVGELPHP6pB
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "OperationDenied",
            "Message": "无查看权限, 请检查"
        },
        "RequestId": "s1692325082060040872"
    }
}
```

