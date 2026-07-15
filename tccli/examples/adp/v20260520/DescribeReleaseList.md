**Example 1: DescribeReleaseList**

查询发布列表

Input: 

```
tccli adp DescribeReleaseList --cli-unfold-argument  \
    --AppId 206************5184 \
    --PageNumber 0 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "ReleaseList": [
            {
                "CanExport": true,
                "CanRollback": true,
                "Description": "我的发布信息",
                "FailCount": 0,
                "Reason": "",
                "ReleaseId": "206*************232",
                "ReleaseVersion": "v20260602164208",
                "Status": 3,
                "StatusDescription": "发布成功",
                "SuccessCount": 0,
                "UpdateTime": "1780389728",
                "Updater": "wu******g"
            }
        ],
        "TotalCount": 2,
        "RequestId": "838ba339-d78e-4162-a1a2-c69371cd0e3f"
    }
}
```

