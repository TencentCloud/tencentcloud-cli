**Example 1: 获取集群状态历史**



Input: 

```
tccli dlc GetRayClusterHistory --cli-unfold-argument  \
    --Id raycluster-20260602191330-yej4 \
    --Page 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "ClusterId": "171",
                "ClusterName": "aidanyxu-test",
                "Event": "FAIL",
                "FromState": "STARTING",
                "Id": 885,
                "Message": "Failed to submit RayCluster raycluster-20260602191330-yej4 to Kubernetes: SubPathMode is set but SubPath is empty, paramVolume: {\"FileSystemId\":\"cfs-eikhdf8b\",\"VolumeSubPath\":\"/\",\"SubPathMode\":\"subPath\",\"SubPath\":\"\",\"MountPath\":\"/d\",\"FSId\":\"enyuf3td\",\"Host\":\"10.0.0.2\",\"PersistVolumeName\":\"raycluster-20260602191330-yej4-cfs-ed05d9b0567ba7c87a52af666bcc09f3\",\"VpcId\":\"vpc-nocygw15\",\"SubnetId\":\"subnet-p1zbl2ns\",\"Uin\":\"700002655693\",\"Region\":\"ap-guangzhou\",\"VolumeMountMode\":\"ReadOnly\"}",
                "ToState": "FAILED",
                "TransitionTime": 1780402599183
            }
        ],
        "Page": 1,
        "PageSize": 10,
        "Total": 4,
        "TotalPages": 1,
        "RequestId": "b34b3dda-1801-4339-ae80-9b74eaa55b19"
    }
}
```

