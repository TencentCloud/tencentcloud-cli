**Example 1: 批量修改记录**

批量修改记录

Input: 

```
tccli dnspod ModifyRecordBatchV3 --cli-unfold-argument  \
    --ModifyRecordList.0.RecordId 16415220 \
    --ModifyRecordList.0.RecordLine 电信
```

Output: 
```
{
    "Response": {
        "JobId": 20000060,
        "RequestId": "0dc0f993-244f-4c38-9311-fa333e216c01"
    }
}
```

