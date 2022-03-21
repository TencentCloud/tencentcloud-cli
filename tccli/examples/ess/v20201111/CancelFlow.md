**Example 1: CancelFlow**



Input: 

```
tccli ess CancelFlow --cli-unfold-argument  \
    --Operator.OpenId xx \
    --Operator.ClientIp xx \
    --Operator.UserId xx \
    --Operator.Channel xx \
    --Operator.ProxyIp xx \
    --FlowId xx \
    --CancelMessage xx
```

Output: 
```
{
    "Response": {
        "RequestId": "xxxxx"
    }
}
```

**Example 2: 撤销流程样例**



Input: 

```
tccli ess CancelFlow --cli-unfold-argument  \
    --Operator.UserId yDxMkUyKQDWLhGUuO4zjE8VI2JmKxPkk \
    --FlowId yDR1HUUgygjb689nUuO4zjE8imAxVxl3 \
    --CancelMessage 字符串
```

Output: 
```
{
    "Response": {
        "RequestId": "85b29b26-a081-44a4-a1dd-104fa651ecc8"
    }
}
```

