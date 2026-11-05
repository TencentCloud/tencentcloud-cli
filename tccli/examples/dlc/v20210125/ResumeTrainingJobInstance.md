**Example 1: 断点续训（克隆实例）**



Input: 

```
tccli dlc ResumeTrainingJobInstance --cli-unfold-argument  \
    --InstanceId raytrain-20261014170006-0ml7 \
    --ResumeCheckpointSubDir sft_ray_training/checkpoint_2026-10-14_19-34-02.520072
```

Output: 
```
{
    "Response": {
        "Instance": {
            "Catalog": "{\"COSVolumes\":[{\"Region\":\"ap-guangzhou\",\"Bucket\":\"dlc-andrew-260200066\",\"VolumeSubPath\":\"/datasets\",\"MountPath\":\"/datas\",\"PersistVolumeName\":\"raytrain-20261014170006-0ml7-cos-010e7bb1bd57c1a232b2c649f794132c\",\"VolumeMountMode\":\"ReadOnly\",\"Source\":\"dataset\",\"Origin\":\"platform_upload\"},{\"Region\":\"ap-guangzhou\",\"Bucket\":\"dlc-andrew-260200066\",\"VolumeSubPath\":\"/checkpoints/raytrain-20261015114628-w0aj\",\"MountPath\":\"/shared\",\"PersistVolumeName\":\"raytrain-20261014170006-0ml7-cos-f9c0344d835f6127328e01e224918c33\",\"VolumeMountMode\":\"ReadWrite\",\"Source\":\"checkpoint\"},{\"Region\":\"ap-guangzhou\",\"Bucket\":\"dlc-andrew-260200066\",\"VolumeSubPath\":\"/checkpoints/raytrain-20261014170006-0ml7\",\"MountPath\":\"/resume-checkpoint\",\"VolumeMountMode\":\"ReadOnly\",\"Source\":\"resume-checkpoint\"}]}",
            "CheckpointMountInfo": {
                "Bucket": "dlc-andrew-260200066",
                "MountPath": "/shared",
                "PlatformManaged": false,
                "Region": "ap-guangzhou",
                "StorageType": "COS",
                "VolumeSubPath": "/checkpoints/raytrain-20261015114628-w0aj"
            },
            "CodePackageUrl": "job-packages/260200066/20261014165440/83a5be10-a634-4ce4-b158-b27e847ad6a3.zip/sft_demo.zip",
            "CreateTime": 1792035991161,
            "Creator": "700002655694",
            "Entrypoint": "bash -c 'cd sft_demo && python -m sft_demo.train_local --storage-path /shared --num-epochs 5000 --learning-rate 0.0002'",
            "Image": "ccr.ccs.tencentyun.com/emr-image/tcray:2.55.1-py311-cpu-torch-lab",
            "InstanceId": "raytrain-20261015114628-w0aj",
            "JobCreateTime": 1792035991161,
            "JobRunningTime": 44,
            "Kind": "CUSTOM_CODE",
            "MlFlowConfig": "{\"MlFlowMode\":\"remote\",\"MlFlowServerId\":\"mlflow-5d8bed2a\"}",
            "Queue": "default",
            "ResourceConfig": "{\"Head\":{\"Name\":\"Head\",\"PodCpu\":2,\"PodMem\":8,\"GpuType\":\"\",\"GpuNum\":0,\"Envs\":[],\"Labels\":[],\"ResourcesLabels\":[],\"Tolerations\":null,\"ResourceType\":\"CPU\",\"InstanceType\":\"\",\"Spec\":2,\"BillingItem\":\"sv_dlc_standard_cu_standard_cu\",\"VideoMemory\":null,\"PodNum\":1,\"HighAvailability\":false,\"LabCu\":null},\"Worker\":[{\"Name\":\"WorkerGroup01\",\"PodCpu\":1,\"PodMem\":4,\"GpuType\":\"\",\"GpuNum\":0,\"Envs\":[],\"Labels\":[],\"ResourcesLabels\":[],\"Tolerations\":null,\"ResourceType\":\"CPU\",\"InstanceType\":\"\",\"Spec\":1,\"BillingItem\":\"sv_dlc_standard_cu_standard_cu\",\"VideoMemory\":null,\"MinPodNum\":1,\"MaxPodNum\":1,\"EnableAutoScaling\":false}]}",
            "ResourcePartitionId": "dlc-p-pcpjozsy",
            "ResumeSourceInstanceId": "raytrain-20261014170006-0ml7",
            "RuntimeEnv": "{\"env_vars\":{\"MLFLOW_TRACKING_URI\":\"http://mlflow-5d8bed2a-mlflow-svc.dlc-p-pcpjozsy.svc.cluster.local:5000\",\"MLFLOW_EXPERIMENT_NAME\":\"sft_demo\",\"HF_MLFLOW_LOG_ARTIFACTS\":\"false\",\"RAY_OVERRIDE_JOB_RUNTIME_ENV\":\"1\",\"MLFLOW_RUN_NAME\":\"raytrain-20261015114628-w0aj\",\"RESUME_CHECKPOINT_DIR\":\"/resume-checkpoint\",\"RESUME_CHECKPOINT_SUBDIR\":\"sft_ray_training/checkpoint_2026-10-14_19-34-02.520072\"},\"pip\":[\"mlflow>=2.10.0\"],\"working_dir\":\"https://common-job-packages-251233710.cos.ap-guangzhou.myqcloud.com/job-packages/260200066/20261014165440/83a5be10-a634-4ce4-b158-b27e847ad6a3.zip/sft_demo.zip?q-sign-algorithm=sha1&q-*k=***************************************sign-time=179203**88%**1792039588&q-key-time=1****35988%3B1792039588&q-header-list=host&q-url-param-list=&q-signature=cf7af337641f858243565a636b1b66e1bef82f82\"}",
            "SpecId": "raytrain-spec-tmw3hv-rw9c",
            "SpecName": "sft_demo",
            "Status": "SUBMITTED",
            "SubAccountName": "700002655694",
            "SubAccountUin": "700002655694"
        },
        "RequestId": "930c8241-570e-4cd7-8e58-7026d9a14da9"
    }
}
```

