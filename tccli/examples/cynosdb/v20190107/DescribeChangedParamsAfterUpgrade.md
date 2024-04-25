**Example 1: 查询升降配运行参数对比**

查询升降配运行参数对比

Input: 

```
tccli cynosdb DescribeChangedParamsAfterUpgrade --cli-unfold-argument  \
    --InstanceId cynosdbmysql-ins-p8dst5v9 \
    --DstCpu 1 \
    --DstMem 1
```

Output: 
```
{
    "Response": {
        "RequestId": "7613eed6-5eb5-4d17-ae69-dd93c44d7ad4",
        "TotalCount": 1,
        "Items": [
            {
                "ParamName": "demoString",
                "NewValue": "demoString",
                "OldValue": "demoString",
                "ValueFunction": "demoString"
            }
        ]
    }
}
```

