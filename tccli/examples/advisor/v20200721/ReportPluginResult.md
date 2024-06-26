**Example 1: 上报插件执行结果**



Input: 

```
tccli advisor ReportPluginResult --cli-unfold-argument  \
    --ArchId arch-nnqlpvnf \
    --Username tairyao \
    --RequestFrom ArchAdmin \
    --Result SessionId: xxx|执行成功
```

Output: 
```
{
    "Response": {
        "RequestId": "5a2a6387-e36d-47de-901a-166664fd6f3c"
    }
}
```

