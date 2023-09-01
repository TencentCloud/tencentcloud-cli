**Example 1: 创建并返回出证报告**

通过已完成签署的流程FlowId，发起出证请求，获取出证报告的ID。

Input: 

```
tccli ess CreateFlowEvidenceReport --cli-unfold-argument  \
    --FlowId yDR0PU**********K5ccC \
    --Operator.UserId yDx************************AcC
```

Output: 
```
{
    "Response": {
        "ReportId": "yDx************************AyF",
        "RequestId": "s166*********616",
        "Status": "EvidenceStatusSuccess"
    }
}
```

**Example 2: 错误示例：流程未签署完，请求出证失败**

流程FlowId必须处于全部签署完成的状态，否则请求将无法成功。

Input: 

```
tccli ess CreateFlowEvidenceReport --cli-unfold-argument  \
    --FlowId yDR0PU**********K5ccC \
    --Operator.UserId yDx************************AcC
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "OperationDenied.FlowStatusForbid",
            "Message": "当前流程状态不支持出证"
        },
        "RequestId": "s1692***********72"
    }
}
```

