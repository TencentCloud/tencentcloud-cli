**Example 1: 获取漏洞视角的漏洞风险列表**

获取漏洞视角的漏洞风险列表

Input: 

```
tccli csip DescribeRiskCenterVULViewVULRiskList --cli-unfold-argument  \
    --MemberId abc \
    --Filter.Limit 0 \
    --Filter.Offset 0 \
    --Filter.Order abc \
    --Filter.By abc \
    --Filter.Filters.0.Name abc \
    --Filter.Filters.0.Values abc \
    --Filter.Filters.0.OperatorType 0 \
    --Filter.StartTime abc \
    --Filter.EndTime abc \
    --Tags.0.TagKey abc \
    --Tags.0.TagValue abc
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "Data": [
            {
                "Port": "abc",
                "NoHandleCount": 0,
                "Level": "abc",
                "Component": "abc",
                "RecentTime": "abc",
                "FirstTime": "abc",
                "AffectAssetCount": 1,
                "Id": "abc",
                "From": "abc",
                "Index": "abc",
                "VULType": "abc",
                "VULName": "abc",
                "CVE": "abc",
                "Describe": "abc",
                "Payload": "abc",
                "AppName": "abc",
                "References": "abc",
                "AppVersion": "abc",
                "VULURL": "abc",
                "Nick": "abc",
                "AppId": "abc",
                "Uin": "abc",
                "Fix": "abc",
                "EMGCVulType": 0
            }
        ],
        "LevelLists": [
            {
                "Value": "abc",
                "Text": "abc"
            }
        ],
        "FromLists": [
            {
                "Value": "abc",
                "Text": "abc"
            }
        ],
        "VULTypeLists": [
            {
                "Value": "abc",
                "Text": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

