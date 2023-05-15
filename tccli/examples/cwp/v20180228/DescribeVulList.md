**Example 1: 获取指定分类和状态的漏洞列表**

获取指定分类和状态的漏洞列表数据

Input: 

```
tccli cwp DescribeVulList --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "VulInfoList": [
            {
                "Ids": "abc",
                "Name": "abc",
                "Status": 1,
                "VulId": 1,
                "PublishTime": "abc",
                "LastTime": "abc",
                "HostCount": 1,
                "Level": 1,
                "From": 1,
                "Descript": "abc",
                "PublishTimeWisteria": "abc",
                "NameWisteria": "abc",
                "DescriptWisteria": "abc",
                "StatusStr": "abc",
                "CveId": "abc",
                "CvssScore": 0,
                "Labels": "abc",
                "FixSwitch": 1,
                "TaskId": 1,
                "IsSupportDefense": 1,
                "DefenseAttackCount": 1,
                "FirstAppearTime": "abc",
                "VulCategory": 1,
                "AttackLevel": 1,
                "FixNoNeedRestart": true
            }
        ],
        "TotalCount": 1,
        "FollowVulCount": 1,
        "RequestId": "abc"
    }
}
```

