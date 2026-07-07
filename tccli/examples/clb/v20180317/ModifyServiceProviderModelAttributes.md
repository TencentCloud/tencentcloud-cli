**Example 1: 修改模型支持的多模态能力**

修改模型支持的多模态能力

Input: 

```
tccli clb ModifyServiceProviderModelAttributes --cli-unfold-argument  \
    --ServiceProviderId byok-qhygv05l \
    --ModelName gpt-4o \
    --InputModalities text
```

Output: 
```
{
    "Response": {
        "RequestId": "d8264fac-0eaa-4981-b63c-dec6df756770"
    }
}
```

