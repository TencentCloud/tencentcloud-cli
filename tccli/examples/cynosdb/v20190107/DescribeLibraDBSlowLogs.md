**Example 1: 查询只读分析引擎慢日志明细**

查询只读分析引擎慢日志明细

Input: 

```
tccli cynosdb DescribeLibraDBSlowLogs --cli-unfold-argument  \
    --InstanceId libradb-ins-i4vsg0tw \
    --StartTime 1753171200 \
    --EndTime 1753171200
```

Output: 
```
{
    "Response": {
        "RequestId": "billing-request-id-77800646"
    }
}
```

