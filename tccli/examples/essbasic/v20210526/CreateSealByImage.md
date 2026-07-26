**Example 1: 创建企业电子印章**



Input: 

```
tccli essbasic CreateSealByImage --cli-unfold-argument  \
    --Agent.AppId yDtKBUUckpf4cgufUuWZO6XBnuF44TXA \
    --Agent.ProxyOrganizationOpenId 123321 \
    --Agent.ProxyOperator.OpenId 123321 \
    --SealName ceshi \
    --SealSize 42_42 \
    --GenerateSource SealGenerateSourceSystem \
    --SealType OTHER
```

Output: 
```
{
    "Response": {
        "ImageUrl": "https://file.test.ess.tencent.cn/bresource/resource/resource/0/0.PNG?hkey=fa8b8ce5d7dcf25fc59ffb546fd5cbaf65cb80b79d479c2bda0b9bb91c68019639fc18b2b20f3bf71fd29fb6b3080b622c1d08678eb5baa8dfa64a9d706d86dc88139a296aec0465fa603bb9bee4c68aa2537f19594b55bf5e2b6833d66be0c41647b4dcfd395697586d12538590b898&sign=1cf2a8eacace5317e3f1d9f034b28f02f4f98383d2243d9071e0d4b31747cad2",
        "PreviewFileUrl": "",
        "PreviewPdfUrl": "",
        "SealId": "yD3J7UUckpeq9ku9UED1q6P8DgGXxXR8",
        "SealOperatorVerifyPath": "",
        "SealOperatorVerifyQrcodeUrl": "",
        "RequestId": "18263fb8-9f12-4b46-a646-0807c1442ff2"
    }
}
```

