**Example 1: 拉取发布按钮状态、最后发布时间**

拉取发布按钮状态、最后发布时间

Input: 

```
tccli lke DescribeReleaseInfo --cli-unfold-argument  \
    --BotBizId 1714970520775950336
```

Output: 
```
{
    "Response": {
        "IsUpdated": false,
        "LastTime": "0",
        "Msg": "",
        "RequestId": "32e717aa-a9bf-4bd1-b6b9-54e8e16b50e5",
        "Status": 2
    }
}
```

