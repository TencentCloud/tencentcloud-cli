**Example 1: 查询用户组列表，放开全部来源IP**

查询用户组列表，放开全部来源IP

Input: 

```
tccli dasb DescribeAccessWhiteListRules --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "AccessWhiteListRuleSet": [],
        "RequestId": "xx",
        "AllowAny": true,
        "AllowAuto": false
    }
}
```

**Example 2: 查询用户组列表，未放开全部来源IP**

查询用户组列表，未放开全部来源IP且开启自动添加IP

Input: 

```
tccli dasb DescribeAccessWhiteListRules --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "AccessWhiteListRuleSet": [
            {
                "Source": "xx",
                "Remark": "xx",
                "Id": 1,
                "ModifyTime": "2020-09-22T00:00:00+00:00"
            }
        ],
        "RequestId": "xx",
        "AllowAny": false,
        "AllowAuto": true
    }
}
```

