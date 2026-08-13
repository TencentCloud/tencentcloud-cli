**Example 1: 查询**



Input: 

```
tccli csip DescribeNetAttackSetting --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "AutoInclude": 0,
        "CWPScope": 1,
        "ClusterIDs": [],
        "ExcludeClusterIDs": [
            "cls-051zf14m"
        ],
        "ExcludeInstanceIDs": [
            "ins-o969mktq"
        ],
        "InstanceIDs": [],
        "NetAttackAlarmStatus": 1,
        "NetAttackEnable": 1,
        "TCSSScope": 1,
        "TagIDs": [],
        "RequestId": "46d95d17-1faa-4ed6-9a0b-0a5ba81bb31c"
    }
}
```

