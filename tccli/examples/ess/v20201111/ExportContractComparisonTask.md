**Example 1: 导出合同对比任务详情**

本接口（ExportContractComparisonTask）用于导出指定的合同对比任务的结果文件。任务完成后，用户可根据不同的使用场景，选择导出可视化对比报告（PDF）或结构化差异明细（EXCEL）。

Input: 

```
tccli ess ExportContractComparisonTask --cli-unfold-argument  \
    --Operator.UserId yDwqbUUckp3o2rzmUxHsV0j1FlhYIKo7 \
    --TaskId yDtrrUUckp94goxhUyjVZ8rSEQ0lg7vb \
    --ExportType 1 \
    --Ignore True
```

Output: 
```
{
    "Response": {
        "ExpireTime": 1760182715,
        "RequestId": "s1760182415600292411",
        "ResourceUrl": "https://file.test.ess.tencent.cn/bresource/resource/resource/0/0.PDF?hkey=*****************"
    }
}
```

