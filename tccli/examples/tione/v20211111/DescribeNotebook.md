**Example 1: Notebook详情**



Input: 

```
tccli tione DescribeNotebook --cli-unfold-argument  \
    --Id xx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "NotebookDetail": {
            "ChargeType": "xx",
            "AutomaticStopTime": 0,
            "EndTime": "xx",
            "ChargeStatus": "xx",
            "Status": "xx",
            "UpdateTime": "xx",
            "VpcId": "xx",
            "Tags": [
                {
                    "TagKey": "xx",
                    "TagValue": "xx"
                }
            ],
            "Id": "xx",
            "ResourceGroupId": "xx",
            "SubnetId": "xx",
            "LifecycleScriptId": "xx",
            "RootAccess": true,
            "Name": "xx",
            "DefaultCodeRepoId": "xx",
            "ResourceConf": {
                "Gpu": 1,
                "Cpu": 1,
                "GpuType": "xx",
                "InstanceType": "xx",
                "Memory": 1
            },
            "AutoStopping": true,
            "ResourceGroupName": "xx",
            "LogEnable": true,
            "BillingInfos": [
                "xx"
            ],
            "InstanceTypeAlias": "xx",
            "AdditionalCodeRepoIds": [
                "xx"
            ],
            "DirectInternetAccess": true,
            "CreateTime": "xx",
            "RuntimeInSeconds": 1,
            "VolumeSizeInGB": 1,
            "StartTime": "xx",
            "PodName": "xx",
            "FailureReason": "xx",
            "LogConfig": {
                "TopicId": "xx",
                "LogsetId": "xx"
            }
        }
    }
}
```

