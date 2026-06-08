**Example 1: 查询实例开启索引建议状态**

查询实例是否开启了索引建议

Input: 

```
tccli dbbrain DescribeDatabaseAutonomyStatus --cli-unfold-argument  \
    --InstanceId cmgo-kuaetxyl \
    --Product mongodb \
    --Type AutoIndexAdvice
```

Output: 
```
{
    "Response": {
        "Status": 0,
        "RequestId": "44bfdc2e-d120-4080-8f5d-1f6564e9abdd"
    }
}
```

