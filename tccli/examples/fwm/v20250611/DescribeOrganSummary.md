**Example 1: 查询集团概览**



Input: 

```
tccli fwm DescribeOrganSummary --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "ac3b6531-d7f0-4752-86af-962359fa7ad5",
        "Summary": {
            "AdminCount": 4,
            "AdminInfo": {
                "AppId": "1300846651",
                "MemberId": "mem-1300846651-100011949846",
                "Nickname": "焦糖小蛋糕",
                "Uin": "100011949846"
            },
            "CfwSharerCount": 1,
            "CfwUserCount": 1,
            "GroupName": "焦糖小蛋糕",
            "JoinedMemberCount": 6,
            "MemberLimit": -1,
            "MemberLimitDisplay": "无上限"
        }
    }
}
```

