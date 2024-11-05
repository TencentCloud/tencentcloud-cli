**Example 1: 修改TXT记录**

成功修改TXT记录

Input: 

```
tccli dnspod ModifyTXTRecord --cli-unfold-argument  \
    --Domain 1777.cn \
    --RecordLine 默认 \
    --Value test for txt record \
    --RecordId 16412960 \
    --SubDomain www \
    --TTL 600 \
    --Status ENABLE
```

Output: 
```
{
    "Response": {
        "RecordId": 16412960,
        "RequestId": "2e55974f-37b6-431e-891a-038de497f839"
    }
}
```

**Example 2: 修改非TXT记录**

修改其他类型的记录时报错

Input: 

```
tccli dnspod ModifyTXTRecord --cli-unfold-argument  \
    --Domain 1777.cn \
    --RecordLine 电信 \
    --Value 3495743 \
    --RecordId 16412961 \
    --SubDomain yyy \
    --TTL 600 \
    --Status ENABLE \
    --Remark 这是备注
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameter.RecordIdInvalid",
            "Message": "记录编号错误。"
        },
        "RequestId": "afdeaa85-02b3-41e2-88c0-66fc001aea71"
    }
}
```

