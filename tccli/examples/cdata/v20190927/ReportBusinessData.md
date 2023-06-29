**Example 1: 上报业务数据**



Input: 

```
tccli cdata ReportBusinessData --cli-unfold-argument  \
    --ReportTag 123DFIEKEIO023K491L3 \
    --TotalCount 1231 \
    --DataStr 批量上报的数据多维二维数组，转JSON序列化
```

Output: 
```
{
    "Response": {
        "ResultMessage": "上报成功",
        "RequestId": "c4355c6b-ba6a-4f42-9f74-6632056431cb"
    }
}
```

