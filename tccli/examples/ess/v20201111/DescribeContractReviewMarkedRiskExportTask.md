**Example 1: 查询导出任务结果**



Input: 

```
tccli ess DescribeContractReviewMarkedRiskExportTask --cli-unfold-argument  \
    --Operator.UserId yDRt****y***5**7***4zjEBBXVnuTnA \
    --TaskId yD3aDUU*k**au*n*UusRvfaSfh2BjyG9
```

Output: 
```
{
    "Response": {
        "Status": 4,
        "Url": "https://file.test.ess.tencent.cn/bresource/resource/resource/0/0.XLSX?hkey=8c9a58b90f96e4cda0a051a032d1924d48235338ad86cd451a3f2c47f220a37b74e2a816764c0a2908cb09e8ee73256dc0886f47afa43e83f58a115d35bcb15dadd2c1b0a30076abc3707ec9e198e37167**2********24ac605678e31e6632adac71d544e61b56905b67189be9a2cedf620e0c70d2dc101e48835ca071ee53e66a9c5d160a2e1abdb3a860cc8430c67",
        "RequestId": "b304560f-5a5b-483d-8577-ed202688a8db"
    }
}
```

