**Example 1: 查询任务相关信息**

查询任务相关信息

Input: 

```
tccli tke DescribeTasks --cli-unfold-argument  \
    --Filter.0.Name ClusterId \
    --Filter.0.Values cls-xxxxx \
    --Filter.1.Name TaskType \
    --Filter.1.Values master_upgrade \
    --Latest True
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "Tasks": [
            {
                "LifeState": "xx",
                "TargetObj": "xx",
                "Param": "xx",
                "TaskType": "xx",
                "LastError": "xx",
                "ClusterID": "xx",
                "CreatedAt": "xx",
                "UpdatedAt": "xx",
                "TaskID": "xx"
            }
        ]
    }
}
```

