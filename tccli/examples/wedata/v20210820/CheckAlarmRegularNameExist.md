**Example 1: 检查规则名称是否存在**

检查规则名称是否存在

Input: 

```
tccli wedata CheckAlarmRegularNameExist --cli-unfold-argument  \
    --ProjectId 11022568003970304 \
    --AlarmRegularName test_regular
```

Output: 
```
{
    "Response": {
        "RequestId": "9f2cdb12-cbc8-431a-94e8-c658ae3ca3ac",
        "Data": true
    }
}
```

