**Example 1: 请求示例**

业务接口报错

Input: 

```
tccli billing SetRenewFlagInner --cli-unfold-argument  \
    --OwnerUin 909619400 \
    --OperateUin 909619400 \
    --ProductCode p_tcb \
    --AutoRenewFlag 1 \
    --ReferenceId 23452xxc \
    --ResourceSet.0.SubProductCode sp_tcb_personal \
    --ResourceSet.0.ResourceType sp_tcb_personal \
    --ResourceSet.0.RegionApCode ap-shanghai \
    --ResourceSet.0.ResourceId hello-3gajm6xs52311be0
```

Output: 
```
{
    "Response": {
        "ReferenceId": "23452xxc",
        "RequestId": "84ea5f3b-059d-499c-8f20-249dbdc8c264",
        "ResourceSet": [
            {
                "Message": "http connect timeout",
                "OperateResult": 400102,
                "ResourceId": "hello-3gajm6xs52311be0"
            }
        ]
    }
}
```

