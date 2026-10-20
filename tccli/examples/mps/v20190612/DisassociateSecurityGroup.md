**Example 1: 请求示例**

批量解绑安全组下面关联的输入输出。

Input: 

```
tccli mps DisassociateSecurityGroup --cli-unfold-argument  \
    --Id 018d0be70ed7 \
    --UnattachInOutInfos.0.FlowId 01888fa3c8ce1ea \
    --UnattachInOutInfos.0.InOutId 5578a028fa7a0 \
    --UnattachInOutInfos.0.InOutType Input \
    --UnattachInOutInfos.0.FlowRegion ap-shanghai
```

Output: 
```
{
    "Response": {
        "RequestId": "01888fa3xxce1ea5578a0209a7yy"
    }
}
```

