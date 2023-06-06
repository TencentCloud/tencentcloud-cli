**Example 1: 检查规则名称是否存在**

检查规则名称是否存在

Input: 

```
tccli wedata CheckAlarmRegularNameExist --cli-unfold-argument  \
    --ProjectId 123 \
    --AlarmRegularName test_regular
```

Output: 
```
{
    "Response": {
        "RequestId": "123",
        "Data": true
    }
}
```

