**Example 1: 启动签署流程-电子文档尚未准备好**

在调用此接口时，若流程电子文档尚未准备就绪，将返回相关错误信息。
在此状态下，可以进行重试。
通常建议在调用创建签署流程电子文档接口后等待3秒，再调用此接口以启动签署流程。

Input: 

```
tccli ess StartFlow --cli-unfold-argument  \
    --Operator.UserId yDxM6UyK********QDV8dJUuO4zjEu \
    --FlowId c7b5ca37ae*******2b4c6644
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "OperationDenied.DocumentNoAvailable",
            "Message": "电子文档不可用，请稍后重试。"
        },
        "RequestId": "s1692*******0872"
    }
}
```

**Example 2: 正常启动签署流程**

启动签署流程

Input: 

```
tccli ess StartFlow --cli-unfold-argument  \
    --Operator.UserId yDxM6UyK********QDV8dJUuO4zjEu \
    --FlowId c7b5ca37ae*******2b4c6644
```

Output: 
```
{
    "Response": {
        "Status": "START",
        "RequestId": "s12**********789"
    }
}
```

