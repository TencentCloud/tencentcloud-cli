**Example 1: 更新训练作业配置**



Input: 

```
tccli dlc ModifyTrainingJobSpec --cli-unfold-argument  \
    --SpecId raytrain-spec-tiogqf-yb6e \
    --SpecName xxd \
    --Description sadfafda
```

Output: 
```
{
    "Response": {
        "Spec": {
            "BaseModelName": "Qwen3.5-4B",
            "BaseModelUid": "m-qwen3-5-4b-6a3218e7-7447",
            "Catalog": "{\"CFSVolumes\":null,\"CFSTurboVolumes\":null,\"COSVolumes\":[{\"Region\":\"ap-guangzhou\",\"Bucket\":\"common-job-packages-251233710\",\"VolumeSubPath\":\"/builtin-models/Qwen3.5-4B/v1/\",\"SubPathMode\":null,\"SubPath\":null,\"MountPath\":\"/builtin-models/Qwen3.5-4B/v1\",\"PersistVolumeName\":null,\"VolumeMountMode\":\"ReadOnly\",\"Source\":null},{\"Region\":null,\"Bucket\":\"aidanyxu-cos-260200065\",\"VolumeSubPath\":\"\",\"SubPathMode\":null,\"SubPath\":null,\"MountPath\":\"/\",\"PersistVolumeName\":null,\"VolumeMountMode\":\"ReadWrite\",\"Source\":\"checkpoint\"},{\"Region\":null,\"Bucket\":\"aidanyxu-cos-260200065\",\"VolumeSubPath\":\"\",\"SubPathMode\":\"subPath\",\"SubPath\":\"\",\"MountPath\":\"\",\"PersistVolumeName\":null,\"VolumeMountMode\":null,\"Source\":\"dataset\"}],\"GooseFSVolumes\":null}",
            "Checkpoint": {
                "Catalog": "{\"CFSVolumes\":[],\"COSVolumes\":[{\"Bucket\":\"aidanyxu-cos-260200065\",\"VolumeSubPath\":\"\",\"SubPathMode\":\"subPath\",\"SubPath\":\"\",\"MountPath\":\"/\",\"VolumeMountMode\":\"ReadWrite\",\"Source\":\"checkpoint\"}],\"CFSTurboVolumes\":[],\"GooseFSVolumes\":[]}",
                "MaxKeep": 0,
                "OutputDir": "",
                "SaveFreq": 1,
                "SaveStrategy": "epoch"
            },
            "CheckpointMountInfo": {
                "Bucket": "aidanyxu-cos-260200065",
                "MountPath": "/",
                "PlatformManaged": false,
                "Region": "ap-guangzhou",
                "StorageType": "COS",
                "VolumeSubPath": ""
            },
            "CreateTime": 1784893623242,
            "Creator": "700002655693",
            "Description": "sadfafda",
            "Entrypoint": "python /workspace/ray_post_training_entry.py --num-workers 1 --gpus-per-worker 0 --cpus-per-worker 1",
            "HasRunningInstances": false,
            "InstanceCount": 0,
            "Kind": "POST_TRAINING",
            "MlFlowConfig": "{\"MlFlowMode\":\"local\",\"MlFlowServerOptions\":{\"cors-allowed-origins\":\"*\"}}",
            "Mode": "sft",
            "OutputModelName": "",
            "Priority": 5,
            "Queue": "default",
            "ResourceConfig": "{\"Head\":{\"Name\":\"Head\",\"ResourceType\":\"CPU\",\"BillingItem\":\"\",\"Spec\":2,\"Envs\":[],\"Labels\":[],\"ResourcesLabels\":[],\"HighAvailability\":false,\"PodNum\":1},\"Worker\":[{\"Name\":\"WorkerGroup01\",\"ResourceType\":\"CPU\",\"BillingItem\":\"\",\"Spec\":1,\"Envs\":[],\"Labels\":[],\"ResourcesLabels\":[],\"MinPodNum\":1,\"MaxPodNum\":1}]}",
            "ResourceConfigId": "",
            "ResourcePartitionId": "dlc-p-wdtiljwu",
            "ResourcePartitionName": "leion",
            "RuntimeEnv": "{\"env_vars\":{\"TRAIN_CONFIG_YAML_B64\":\"IyDorq3nu4PphY3nva7vvJpTRlQgKOebkeedo+W+ruiwgykKIyDljaDkvY3nrKYgJHsuLi59IOeUsSBQb3N0VHJhaW5pbmdUZW1wbGF0ZVJlbmRlcmVyIOaMieeUqOaIt+ihqOWNlea4suafk+abv+aNouOAggojIOWOn+eUnyBIdWdnaW5nRmFjZSBUcmFpbmVyICsgdHJsLlNGVFRyYWluZXLvvIzkuI3kvp3otZYgTExhTUEtRmFjdG9yeeOAggoKIyMjIG1ldGhvZApzdGFnZTogc2Z0CmZpbmV0dW5pbmdfdHlwZTogbG9yYSAgICAgICAgICAgICAjIGZ1bGwgfCBsb3JhCmxvcmFfdGFyZ2V0OiBhbGwKbG9yYV9yYW5rOiA4CmxvcmFfYWxwaGE6IDE2CmxvcmFfZHJvcG91dDogMC4wNQoKIyMjIG1vZGVsCm1vZGVsX25hbWVfb3JfcGF0aDogL2J1aWx0aW4tbW9kZWxzL1F3ZW4zLjUtNEIvdjEKdHJ1c3RfcmVtb3RlX2NvZGU6IHRydWUKCiMjIyBkYXRhc2V0CnRyYWluX2ZpbGU6ICAgICAgICAgICAgICAgICAgICAgICMg5pWw5o2u5paH5Lu25ZCN5oiW57ud5a+56Lev5b6ECmRhdGFzZXRfZGlyOiAvd29ya3NwYWNlL2RhdGEKY3V0b2ZmX2xlbjogNDA5NgptYXhfc2FtcGxlczogMTAwMDAwCnByZXByb2Nlc3NpbmdfbnVtX3dvcmtlcnM6IDE2CgojIyMgZXZhbApldmFsX21vZGU6IG5vbmUgICAgICAgICAgICAgICAgICAgICAgICMgbm9uZSB8IHNwbGl0IHwgc2VwYXJhdGUKZXZhbF9zcGxpdF9yYXRpbzogMC4wNSAgICAgICAgICAjIOS7hSBzcGxpdCDmqKHlvI/nlJ/mlYgKZXZhbF9maWxlOiAgICAgICAgICAgICAgICAgICAgICAgICAjIOS7hSBzZXBhcmF0ZSDmqKHlvI/nlJ/mlYgKZXZhbF9kYXRhc2V0X2RpcjogICAgICAgICAgICMg5LuFIHNlcGFyYXRlIOaooeW8j+eUn+aViAoKIyMjIG91dHB1dApvdXRwdXRfZGlyOiAvCiMg5Lqn5Ye65qih5Z6L5ZCN56ew77yI55So5LqO5ZCO57ut5qih5Z6L5rOo5YaM77yJCm91dHB1dF9tb2RlbF9uYW1lOiAKbG9nZ2luZ19zdGVwczogMTAKc2F2ZV9zdHJhdGVneTogImVwb2NoIgpzYXZlX3N0ZXBzOiAxCnNhdmVfdG90YWxfbGltaXQ6IDAKIyDmlq3ngrnnu63orq3vvJp0cnVlIOaXtuS7jiBvdXRwdXRfZGlyIOS4reacgOaWsCBjaGVja3BvaW50IOaBouWkjeiuree7gwpyZXN1bWVfdHJhaW5pbmc6IGZhbHNlCiMg55Sx5bmz5Y+w5riy5p+T77yM5ZCv55SoIE1MZmxvdyDml7bkuLogWyJtbGZsb3ciLCJ0ZW5zb3Jib2FyZCJd77yM5pyq5ZCv55So5pe25Li6IHRlbnNvcmJvYXJkCnJlcG9ydF90bzogWyJtbGZsb3ciLCJ0ZW5zb3Jib2FyZCJdCnJ1bl9uYW1lOiAke1JVTl9OQU1FfQoKIyMjIHRyYWluCnBlcl9kZXZpY2VfdHJhaW5fYmF0Y2hfc2l6ZTogMgpncmFkaWVudF9hY2N1bXVsYXRpb25fc3RlcHM6IDQKZ3JhZGllbnRfY2hlY2twb2ludGluZzogZmFsc2UKbGVhcm5pbmdfcmF0ZTogMS4wRS00Cm51bV90cmFpbl9lcG9jaHM6IDMKbHJfc2NoZWR1bGVyX3R5cGU6IGNvc2luZQp3YXJtdXBfcmF0aW86IDAuMDMKYmYxNjogdHJ1ZQpkZHBfdGltZW91dDogMTgwMDAwMDAwCgojIyMgZGVlcHNwZWVkICjmuLLmn5Pnu5Pmnpzot6/lvoTvvIznlLHlhaXlj6PohJrmnKwgYmFzZTY0IOino+eggeWGmeWHuikKZGVlcHNwZWVkOiAvdG1wL3RyYWluLWNvbmZpZy9kc196My5qc29uCgojIyMgZXZhbApwZXJfZGV2aWNlX2V2YWxfYmF0Y2hfc2l6ZTogMQpldmFsX3N0cmF0ZWd5OiAibm8iICAgICAgICAgICAgICAgIyAibm8iIHwgInN0ZXBzIiB8ICJlcG9jaCIKZXZhbF9zdGVwczogNTAwCg==\",\"DEEPSPEED_CONFIG_B64\":\"ewogICAgInRyYWluX2JhdGNoX3NpemUiOiAiYXV0byIsCiAgICAidHJhaW5fbWljcm9fYmF0Y2hfc2l6ZV9wZXJfZ3B1IjogImF1dG8iLAogICAgImJmMTYiOiB7ImVuYWJsZWQiOiAiYXV0byJ9LAogICAgImdyYWRpZW50X2NsaXBwaW5nIjogImF1dG8iLAogICAgInplcm9fb3B0aW1pemF0aW9uIjogewogICAgICAgICJvZmZsb2FkX29wdGltaXplciI6IHsiZGV2aWNlIjogIm5vbmUifSwKICAgICAgICAib3ZlcmxhcF9jb21tIjogdHJ1ZSwKICAgICAgICAic3RhZ2UiOiAzLAogICAgICAgICJzdWJfZ3JvdXBfc2l6ZSI6IDFFKzksCiAgICAgICAgImNvbnRpZ3VvdXNfZ3JhZGllbnRzIjogdHJ1ZSwKICAgICAgICAicmVkdWNlX2J1Y2tldF9zaXplIjogImF1dG8iLAogICAgICAgICJzdGFnZTNfZ2F0aGVyXzE2Yml0X3dlaWdodHNfb25fbW9kZWxfc2F2ZSI6IHRydWUsCiAgICAgICAgIm9mZmxvYWRfcGFyYW0iOiB7ImRldmljZSI6ICJub25lIn0sCiAgICAgICAgInN0YWdlM19wcmVmZXRjaF9idWNrZXRfc2l6ZSI6ICJhdXRvIiwKICAgICAgICAic3RhZ2UzX3BhcmFtX3BlcnNpc3RlbmNlX3RocmVzaG9sZCI6ICJhdXRvIiwKICAgICAgICAic3RhZ2UzX21heF9saXZlX3BhcmFtZXRlcnMiOiAxRSs5LAogICAgICAgICJzdGFnZTNfbWF4X3JldXNlX2Rpc3RhbmNlIjogMUUrOQogICAgfSwKICAgICJ6ZXJvX2FsbG93X3VudGVzdGVkX29wdGltaXplciI6IHRydWUsCiAgICAiZ3JhZGllbnRfYWNjdW11bGF0aW9uX3N0ZXBzIjogImF1dG8iLAogICAgImZwMTYiOiB7CiAgICAgICAgIm1pbl9sb3NzX3NjYWxlIjogMSwKICAgICAgICAiaW5pdGlhbF9zY2FsZV9wb3dlciI6IDE2LAogICAgICAgICJsb3NzX3NjYWxlIjogMCwKICAgICAgICAiZW5hYmxlZCI6ICJhdXRvIiwKICAgICAgICAibG9zc19zY2FsZV93aW5kb3ciOiAxMDAwLAogICAgICAgICJoeXN0ZXJlc2lzIjogMgogICAgfQp9Cg==\",\"NUM_WORKERS\":\"1\",\"GPUS_PER_WORKER\":\"0\",\"CPUS_PER_WORKER\":\"1\",\"NCCL_DEBUG\":\"WARN\",\"HF_HOME\":\"/workspace/cache/hf\",\"WANDB_DISABLED\":\"true\",\"MLFLOW_TRACKING_URI\":\"$MLFLOW_TRACKING_URI\",\"MLFLOW_EXPERIMENT_NAME\":\"xxd\",\"HF_MLFLOW_LOG_ARTIFACTS\":\"false\"}}",
            "SpecId": "raytrain-spec-tiogqf-yb6e",
            "SpecName": "xxd",
            "Tags": [],
            "TuningParams": {
                "CutoffLen": 4096,
                "DPOBeta": 0.1,
                "DPOLoss": "sigmoid",
                "Epochs": 3,
                "FineTuneType": "lora",
                "GradientAccumulationSteps": 4,
                "GradientCheckPointing": false,
                "LoraAlpha": 16,
                "LoraDropout": 0.05,
                "LoraRank": 8,
                "LoraTarget": "all",
                "LrScheduler": "cosine",
                "PerDeviceBatchSize": 2,
                "TrainingMode": "balanced",
                "WarmupRatio": 0.03
            },
            "UpdateTime": 1784893623242
        },
        "RequestId": "72056b91-6068-4df5-a39e-a24fc8512bc6"
    }
}
```

