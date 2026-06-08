**Example 1: 实例开启与关闭索引建议**

实例开启与关闭索引建议，开启索引推荐功能后，系统将抽样采集该实例的慢查日志和少量元数据信息用于智能分析，数据仅用于索引优化建议

Input: 

```
tccli dbbrain UpdateDatabaseAutonomyStatus --cli-unfold-argument  \
    --InstanceId cmgo-kuaetxyl \
    --Product mongodb \
    --Type AutoIndexAdvice \
    --Status 1
```

Output: 
```
{
    "Response": {
        "Status": 1,
        "RequestId": "5c1bc677-4ddc-4004-8981-fe4f495efdea"
    }
}
```

