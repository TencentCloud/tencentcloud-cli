**Example 1: 为资源绑定标签解除配额**

此接口为预先申请配额后，流程异常导致不能创建给资源打标签请求时调用来释放已经申请的配额。

Input: 

```
tccli tag TagResourcesDeallocateQuotas --cli-unfold-argument  \
    --ResourceTypeQuotasList.0.ResourceType qcs::redis:ap-beijing::instance/* \
    --ResourceTypeQuotasList.0.Quotas 5 \
    --Tags.0.TagKey k \
    --Tags.0.TagValue v
```

Output: 
```
{
    "Response": {
        "RequestId": "cf35716d-0fb2-4623-835a-0209xxxxxxx"
    }
}
```

