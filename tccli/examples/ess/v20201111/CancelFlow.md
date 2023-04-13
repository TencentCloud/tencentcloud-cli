**Example 1: 撤销签署流程样例**

撤销单个签署流程

Input: 

```
tccli ess CancelFlow --cli-unfold-argument  \
    --Operator.UserId yDxMkUy***************JmKxPkk \
    --FlowId yDR1HUU***************JjE8imAxVxl3 \
    --CancelMessage 字符串
```

Output: 
```
{
    "Response": {
        "RequestId": "85b29b***************651ecc8"
    }
}
```

