**Example 1: 请求示例**

批量解绑安全组下面关联的输入输出。

Input: 

```
tccli mps DisassociateSecurityGroup --cli-unfold-argument  \
    --Id abc \
    --UnattachInOutInfos.0.FlowId abc \
    --UnattachInOutInfos.0.InOutId abc \
    --UnattachInOutInfos.0.InOutType abc \
    --UnattachInOutInfos.0.FlowRegion abc
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

