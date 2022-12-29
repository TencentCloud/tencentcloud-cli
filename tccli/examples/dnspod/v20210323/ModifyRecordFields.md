**Example 1: 修改记录可选字段**

 

Input: 

```
tccli dnspod ModifyRecordFields --cli-unfold-argument  \
    --Domain modify1.com \
    --RecordId 15690732 \
    --FieldList.0.Key weight \
    --FieldList.0.Value 20
```

Output: 
```
{
    "Response": {
        "RequestId": "b3e412d3-0eeb-4b05-815c-86763b9d72aa",
        "RecordId": 15690732
    }
}
```

