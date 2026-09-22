**Example 1: 调用示例**



Input: 

```
tccli live CreateLiveSmartEraseTemplate --cli-unfold-argument  \
    --TemplateName SmartName111 \
    --Type illegal audio \
    --Description SmartNameDesc \
    --AuditConfId 0 \
    --PrivacyProtection blur face
```

Output: 
```
{
    "Response": {
        "TemplateId": 8390364,
        "RequestId": "11f23d53-613c-43ff-8f8b-81e3aef57952"
    }
}
```

