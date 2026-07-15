**Example 1: 导出审查结果和摘要 xlsx 文件**



Input: 

```
tccli ess ExportContractReviewResult --cli-unfold-argument  \
    --Operator.UserId yDtzDUUckpfhotltUxpgD3IvZBJB10dg \
    --TaskId yDtzZUUckpf8wewlUx7RX5uSd4QXIcRI \
    --FileType 2
```

Output: 
```
{
    "Response": {
        "RequestId": "57036460-8ab0-4a0f-b6ca-ec6e4f6cff57",
        "Url": "https://file.test.ess.tencent.cn/bresource/resource/resource/0/0.XLSX?hkey=533ef16b1c16d1f16060554ea3982785c3a30eda68f5c00f6947c7695feb18f97f24e189b77d14350036e89bca11f153f0ddf7c847233dd099d4ee826202371435d8080ec05323e868f41f14676d745a836d2064286b79c812144daaf68f1d661f87f3c43b04b61599a0630dafdef064b741be6c1dba5ab2528bdadfddfcca19e4c8dd5d57c6f61de3a7b186dde961d990bfa7e9fef5bd9a6169b8e1f381789a"
    }
}
```

**Example 2: 导出带批注的审查文件**



Input: 

```
tccli ess ExportContractReviewResult --cli-unfold-argument  \
    --Operator.UserId yDtzDUUkpfhotltUxD3IvZBJB10dg \
    --TaskId yDtzZUckpf8wwlUx7RX5ud4QXIcRI \
    --FileType 1
```

Output: 
```
{
    "Response": {
        "RequestId": "27419bd6-09bf-459d-b514-295964b7478a",
        "Url": "https://file.ess.tencent.cn/bresource/resource/resource/0/0.DOCX?hkey=533ef16b1c16d1f16060554ea3982785c3a30eda68f5c00f6947c7695feb18f9632ebfb577efc74e9b00949c2a27818dc99723b96edadd6266ca2a46f49ee8a6915a01f702b1932ca4b6687198aca50f02e6f9d61c8c32fac3df3741e6e9c032"
    }
}
```

