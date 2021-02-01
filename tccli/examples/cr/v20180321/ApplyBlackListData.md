**Example 1: 提交黑名单申请**



Input: 

```
tccli cr ApplyBlackListData --cli-unfold-argument  \
    --Module account \
    --Operation ApplyBlackList \
    --BlackList.0.BlackType 01 \
    --BlackList.0.OperType A \
    --BlackList.0.BlackValue 13312345233 \
    --BlackList.0.BlackDescription 输入示例
```

Output: 
```
{
    "Response": {
        "RequestId": "13ca0b60-ff5g-43e2-9123-b9361bf0f93e"
    }
}
```

