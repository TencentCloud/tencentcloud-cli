**Example 1: 创建并返回出证报告**

通过已完成签署的流程FlowId，发起出证请求，获取出证报告的ID。

Input: 

```
tccli essbasic CreateChannelFlowEvidenceReport --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyAppId  \
    --FlowId yDSLVUUckpo1c11xUxtOq8cvKy24by9M
```

Output: 
```
{
    "Response": {
        "ReportId": "yDSLVUUckpo3nva8UEnf33kvzHQ19GcL",
        "Status": "EvidenceStatusSuccess",
        "ReportUrl": "",
        "RequestId": "78062b87-6571-4f9a-b7a2-ba2d8d6c6698"
    }
}
```

**Example 2: 流程未签署完，请求出证失败**

流程FlowId必须处于全部签署完成的状态，否则请求将无法成功。

Input: 

```
tccli essbasic CreateChannelFlowEvidenceReport --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyAppId  \
    --FlowId yDSLVUUckpo1c11xUxtOq8cvKy24by9M
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "OperationDenied.FlowStatusForbid",
            "Message": "当前流程状态不支持出证"
        },
        "RequestId": "78062b87-6571-4f9a-b7a2-ba2d8d6c6698"
    }
}
```

