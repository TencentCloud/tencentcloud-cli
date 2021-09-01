**Example 1: 查询Notebook实例**



Input: 

```
tccli tione DescribeNotebookInstance --cli-unfold-argument  \
    --NotebookInstanceName test
```

Output: 
```
{
    "Response": {
        "RequestId": "b869fa8e-f3b8-449b-a356-83e44204942b",
        "NotebookInstanceName": "test",
        "InstanceType": "TI.SMALL2.1core2g",
        "RoleArn": "qcs::cam::uin/20548499:roleName/TIONE_QCSRole",
        "DirectInternetAccess": "Enabled",
        "RootAccess": "Enabled",
        "SubnetId": "subnet-xxx",
        "VolumeSizeInGB": 10,
        "FailureReason": "InternalError.GetRoleError-[QC_STS] role not exist",
        "CreationTime": "2019-11-22 10:15:52",
        "LastModifiedTime": "2019-11-22 10:17:48",
        "LogUrl": "https://console.cloud.tencent.com/cls/search?region=ap-guangzhou&logset_id=e9c9d84c-b9bc-4b08-a7c5-93441ce4e790&topic_id=29728e56-8076-4100-808e-c22bf69d4c47&product=tione&start_time=2019-11-21+10%3A31%3A21&end_time=2019-11-22+10%3A31%3A21&query=app%3Anotebook-fzdfj62ktj",
        "NotebookInstanceStatus": "Failed",
        "InstanceId": "notebook-fzdfj62ktj",
        "LifecycleScriptsName": "aaa",
        "ClsAccess": "Enabled"
    }
}
```

