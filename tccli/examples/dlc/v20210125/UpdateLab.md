**Example 1: UpdateLab**

更新实验室配置

Input: 

```
tccli dlc UpdateLab --cli-unfold-argument  \
    --Catalog {"CFSVolumes":[],"COSVolumes":[{"Bucket":"aidanyxu-cq-10-1414839048","VolumeSubPath":"/aidanyxu","SubPathMode":"subPath","SubPath":"","MountPath":"/nmt/data/aidanyxu","VolumeMountMode":"ReadWrite"}],"CFSTurboVolumes":[{"FileSystemId":"cfs-4b9fc65cb","VolumeSubPath":"/","SubPathMode":"subPath","SubPath":"","MountPath":"/mnt/data/aidanyxu/aidanyx","VolumeMountMode":"ReadWrite"}],"GooseFSVolumes":[]} \
    --Id raylab-20260818143841-zgd5 \
    --Image aidanyxu.tencentcloudcr.com/andrewmao/dlctest:tcray2.57.0-py311-cpu \
    --ImagePullType CUSTOM \
    --Name aidanyxu_Cos \
    --PersistentWorkDir.Enabled False \
    --Priority 5 \
    --Queue default \
    --ResourceConfig {"Head":{"Name":"Head","ResourceType":"CPU","BillingItem":"sv_dlc_standard_cu_standard_cu","Spec":1,"Envs":[],"Labels":[],"ResourcesLabels":[],"HighAvailability":false,"PodNum":1,"LabCu":1},"Worker":[{"Name":"WorkerGroup01","ResourceType":"CPU","BillingItem":"sv_dlc_standard_cu_standard_cu","Spec":1,"Envs":[],"Labels":[],"ResourcesLabels":[],"MinPodNum":1,"MaxPodNum":1,"EnableAutoScaling":false}]} \
    --ResourcePartitionId dlc-p-gymyiibl \
    --Tags.0.TagKey dlctest \
    --Tags.0.TagValue ture
```

Output: 
```
{
    "Response": {
        "Id": "raylab-20260818143841-zgd5",
        "Type": "RAY_LAB",
        "Name": "aidanyxu_Cos",
        "ResourcePartitionId": "dlc-p-gymyiibl",
        "ResourcePartitionName": "test_qzzhu_1",
        "Queue": "default",
        "AppId": 1414839048,
        "Uin": "100047465867",
        "SubAccountUin": "100047774296",
        "SubAccountName": "aidanyxu",
        "Status": "STOPPED",
        "CreateTime": 1787035121696,
        "UpdateTime": 1791980289130,
        "ResourceConfig": "{\"Head\":{\"Name\":\"Head\",\"PodCpu\":1,\"PodMem\":4,\"GpuType\":\"\",\"GpuNum\":0,\"Envs\":[],\"Labels\":[],\"ResourcesLabels\":[],\"Tolerations\":null,\"ResourceType\":\"CPU\",\"InstanceType\":\"\",\"Spec\":1,\"BillingItem\":\"sv_dlc_standard_cu_standard_cu\",\"VideoMemory\":null,\"PodNum\":1,\"HighAvailability\":false,\"LabCu\":1},\"Worker\":[{\"Name\":\"WorkerGroup01\",\"PodCpu\":1,\"PodMem\":4,\"GpuType\":\"\",\"GpuNum\":0,\"Envs\":[],\"Labels\":[],\"ResourcesLabels\":[],\"Tolerations\":null,\"ResourceType\":\"CPU\",\"InstanceType\":\"\",\"Spec\":1,\"BillingItem\":\"sv_dlc_standard_cu_standard_cu\",\"VideoMemory\":null,\"MinPodNum\":1,\"MaxPodNum\":1,\"EnableAutoScaling\":false}]}",
        "Image": "aidanyxu.tencentcloudcr.com/andrewmao/dlctest:tcray2.57.0-py311-cpu",
        "Catalog": "{\"CFSVolumes\":[],\"CFSTurboVolumes\":[{\"FileSystemId\":\"cfs-4b9fc65cb\",\"VolumeSubPath\":\"/\",\"SubPathMode\":\"subPath\",\"SubPath\":\"\",\"MountPath\":\"/mnt/data/aidanyxu/aidanyx\",\"FSId\":\"b9fc65cb\",\"Host\":\"10.0.0.241\",\"PersistVolumeName\":\"raylab-20260818143841-zgd5-cfs-turbo-9ba94d8256db98f824603e2c05337de0\",\"VpcId\":\"vpc-12vmf6nr\",\"SubnetId\":\"subnet-64k425ka\",\"CcnId\":\"-\",\"NetworkInterface\":\"VPC\",\"Uin\":\"100047465867\",\"Region\":\"ap-chongqing\",\"VolumeMountMode\":\"ReadWrite\",\"Source\":null,\"AutoCreateSubDir\":null}],\"COSVolumes\":[{\"Region\":\"ap-chongqing\",\"Bucket\":\"aidanyxu-cq-10-1414839048\",\"CustomerClusterSecret\":null,\"VolumeSubPath\":\"/aidanyxu\",\"SubPathMode\":\"subPath\",\"SubPath\":\"\",\"MountPath\":\"/nmt/data/aidanyxu\",\"PersistVolumeName\":\"raylab-20260818143841-zgd5-cos-4aa3e6026b24e974130ab46d419bbf8a\",\"VolumeMountMode\":\"ReadWrite\",\"Source\":null,\"Origin\":null}],\"GooseFSVolumes\":[]}",
        "ImagePullType": "Custom",
        "Priority": 5,
        "Tags": [
            {
                "TagKey": "dlctest",
                "TagValue": "ture"
            }
        ],
        "Services": [
            {
                "Key": "JUPYTER"
            }
        ],
        "PersistentWorkDir": {
            "Enabled": false
        },
        "EnableToken": false,
        "RequestId": "effa12b3-89ae-4a83-acd8-a461fc4a8abd"
    }
}
```

