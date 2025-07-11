**Example 1: 1**



Input: 

```
tccli csip DescribeAccessKeyRisk --cli-unfold-argument  \
    --Filter.Limit 1
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "AccessKey": "AKIDX***13DJ",
                "AccessKeyID": 10075,
                "AccessKeyRemark": "test",
                "AppID": 1256299843,
                "CheckStatus": 0,
                "Description": "应该删除长期未使用AK密钥，即使AK被禁用了也应该删除",
                "Evidence": "",
                "ID": 141,
                "Level": 4,
                "Name": "应该删除长期未使用AK密钥",
                "Nickname": "飞快的云镜",
                "RiskRuleID": 2,
                "RiskTime": "2025-03-13 14:01:30",
                "RiskType": 0,
                "Status": 0,
                "SubNickname": "dorahe",
                "SubUin": "100030819418",
                "Tag": [],
                "Type": 1,
                "Uin": "100004506473"
            }
        ],
        "RequestId": "927e370e-9aeb-454e-9854-32224937c581",
        "Total": 142
    }
}
```

