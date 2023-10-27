**Example 1: 空示例**

空示例

Input: 

```
tccli csip DescribeRiskCenterAssetViewVULRiskList --cli-unfold-argument  \
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
                "AffectAsset": "abc",
                "Level": "abc",
                "InstanceType": "abc",
                "Component": "abc",
                "Service": "abc",
                "RecentTime": "abc",
                "FirstTime": "abc",
                "Status": 1,
                "Id": "abc",
                "Index": "abc",
                "InstanceId": "abc",
                "InstanceName": "abc",
                "AppId": "abc",
                "Nick": "abc",
                "Uin": "abc",
                "VULType": "abc",
                "Port": "abc",
                "Describe": "abc",
                "AppName": "abc",
                "References": "abc",
                "AppVersion": "abc",
                "VULURL": "abc",
                "VULName": "abc",
                "CVE": "abc",
                "Fix": "abc",
                "POCId": "abc",
                "From": "abc",
                "CWPVersion": 0,
                "IsSupportRepair": true,
                "IsSupportDetect": true,
                "InstanceUUID": "abc",
                "Payload": "abc",
                "EMGCVulType": 0
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
        "InstanceTypeLists": [
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

