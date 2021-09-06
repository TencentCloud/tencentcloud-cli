**Example 1: 查询活动记录信息**

查询活动记录信息

Input: 

```
tccli tcb DescribeActivityRecord --cli-unfold-argument  \
    --ActivityIdList 1 \
    --ChannelToken 123 \
    --Channel qc_console \
    --Status 1 \
    --Statuses 1 \
    --IsDeletedList 1
```

Output: 
```
{
    "Response": {
        "RequestId": "51a33e48-a808-4fe7-8c02-4e7be5245351",
        "ActivityRecords": []
    }
}
```

