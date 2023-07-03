**Example 1: 批量删除解析记录**

 

Input: 

```
tccli dnspod DeleteRecordBatch --cli-unfold-argument  \
    --RecordIdList 21213
```

Output: 
```
{
    "Response": {
        "RequestId": "84be1418-2081-41d9-8192-e8e0258f7daa",
        "JobId": 1701629,
        "DetailList": [
            {
                "DomainId": 12620276,
                "Domain": "batchremove.com",
                "Error": null,
                "Status": "waiting",
                "Operation": "remove",
                "RecordList": "解析记录数组，json 序列化的形式"
            }
        ]
    }
}
```

