**Example 1: 创建商业智能平面文件**



Input: 

```
tccli sqlserver CreateBusinessIntelligenceFile --cli-unfold-argument  \
    --Remark aa \
    --FileURL http://xxxxxxxx.cos.ap-guangzhou.myqcloud.com/test.xlsx \
    --InstanceId mssqlbi-fo2dwujt \
    --FileType FLAT
```

Output: 
```
{
    "Response": {
        "FileTaskId": "test.xlsx",
        "RequestId": "9f36fb2e-ae6b-4d18-b1b3-a79111ce4b33"
    }
}
```

