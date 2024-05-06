**Example 1: 空示例**

空示例

Input: 

```
tccli csip DescribeRiskCenterAssetViewCFGRiskList --cli-unfold-argument  \
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
                "Id": "abc",
                "CFGName": "abc",
                "CheckType": "abc",
                "InstanceId": "abc",
                "InstanceName": "abc",
                "InstanceType": "abc",
                "AffectAsset": "abc",
                "Level": "abc",
                "FirstTime": "abc",
                "RecentTime": "abc",
                "From": "abc",
                "Status": 0,
                "CFGSTD": "abc",
                "CFGDescribe": "abc",
                "CFGFix": "abc",
                "CFGHelpURL": "abc",
                "Index": "abc",
                "AppId": "abc",
                "Nick": "abc",
                "Uin": "abc"
            }
        ],
        "StatusLists": [
            {
                "Value": "abc",
                "Text": "abc"
            }
        ],
        "LevelLists": [
            {
                "Value": "abc",
                "Text": "abc"
            }
        ],
        "CFGNameLists": [
            {
                "Value": "abc",
                "Text": "abc"
            }
        ],
        "CheckTypeLists": [
            {
                "Value": "abc",
                "Text": "abc"
            }
        ],
        "InstanceTypeLists": [
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
        "RequestId": "abc"
    }
}
```

