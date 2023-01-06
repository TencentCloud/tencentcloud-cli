**Example 1: 查询在线客服记录示例**

获取包括全媒体和文本会话两种类型的服务记录。

Input: 

```
tccli ccc DescribeIMCdrs --cli-unfold-argument  \
    --SdkAppId 1400000000 \
    --StartTimestamp 1603877878 \
    --EndTimestamp 1603877879
```

Output: 
```
{
    "Response": {
        "IMCdrs": [
            {
                "Id": "12933",
                "Duration": 100,
                "EndStatus": 1,
                "Nickname": "bar",
                "Type": 2,
                "StaffId": "foo@tencent.com",
                "Timestamp": 1632814604,
                "SessionId": "87fa1d7a-4194-4f2a-83dc-d7c293411720",
                "SkillGroupId": "1001",
                "SkillGroupName": "bar",
                "Satisfaction": {
                    "Id": 1,
                    "Label": "满意"
                }
            }
        ],
        "TotalCount": 1,
        "RequestId": "66fa1d7a-4194-4f2a-73dc-d7c293411890"
    }
}
```

