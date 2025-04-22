**Example 1: 查询用户组列表，放开全部来源IP**

查询用户组列表，放开全部来源IP

Input: 

```
tccli bh DescribeAccessWhiteListRules --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "AccessWhiteListRuleSet": [],
        "RequestId": "b8ebf0b3-ecf5-49bf-9f9d-86341c4072f1",
        "AllowAny": true,
        "AllowAuto": false
    }
}
```

**Example 2: 查询用户组列表，未放开全部来源IP**

查询用户组列表，未放开全部来源IP且开启自动添加IP

Input: 

```
tccli bh DescribeAccessWhiteListRules --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "AccessWhiteListRuleSet": [
            {
                "Source": "127.0.0.1",
                "Remark": "",
                "Id": 1,
                "ModifyTime": "2020-09-22T00:00:00+00:00"
            }
        ],
        "RequestId": "b8ebf0b3-ecf5-49bf-9f9d-86341c4072f1",
        "AllowAny": false,
        "AllowAuto": true
    }
}
```

