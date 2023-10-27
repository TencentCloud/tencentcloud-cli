**Example 1: 查询集群检查定时配置**

查询集群检查定时配置

Input: 

```
tccli tcss DescribeClusterCheckTimerSetting --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Status": true,
        "ClusterIDs": [
            "abc"
        ],
        "CycleDay": 1,
        "ScanTimeBegin": "abc",
        "ScanTimeEnd": "abc",
        "ScanScope": 1,
        "RequestId": "abc"
    }
}
```

