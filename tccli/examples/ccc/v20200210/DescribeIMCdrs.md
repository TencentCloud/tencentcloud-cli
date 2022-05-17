**Example 1: 查询在线客服记录示例**



Input: 

```
tccli ccc DescribeIMCdrs --cli-unfold-argument  \
    --InstanceId 11 \
    --StartTimestamp 1603877878 \
    --EndTimestamp 1603877879
```

Output: 
```
{
    "Response": {
        "IMCdrs": [
            {
                "Type": 2,
                "Timestamp": 1632814604,
                "SkillGroupName": "bar",
                "EndStatus": 1,
                "SessionId": "87fa1d7a-4194-4f2a-83dc-d7c293411720",
                "StaffId": "foo@tencent.com",
                "Duration": 100,
                "Nickname": "foo",
                "Id": "12933",
                "SkillGroupId": "1001"
            }
        ],
        "TotalCount": 1,
        "RequestId": "66fa1d7a-4194-4f2a-73dc-d7c293411890"
    }
}
```

