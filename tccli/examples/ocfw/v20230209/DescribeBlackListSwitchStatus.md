**Example 1: 获取封禁列表启用开关**



Input: 

```
tccli ocfw DescribeBlackListSwitchStatus --cli-unfold-argument  \
    --CurrentAppId 0
```

Output: 
```
{
    "Response": {
        "Status": 0,
        "RequestId": "abc"
    }
}
```

