**Example 1: 返回MlFlow关联的训练实例列表**



Input: 

```
tccli dlc ListMlflowServerTrainingInstances --cli-unfold-argument  \
    --ServerId mlflow-7f72b80b
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "BaseModelUid": "m-qwen35-zerodot8b-6a705b58-dc17",
                "Catalog": "{\"CFSVolumes\":null,\"CFSTurboVolumes\":null,\"COSVolumes\":[{\"Region\":\"ap-guangzhou\",\"Bucket\":\"common-job-packages-251233710\",\"VolumeSubPath\":\"/models/m-qwen35-zerodot8b-6a705b58-dc17/v1/\",\"SubPathMode\":null,\"SubPath\":null,\"MountPath\":\"/models/m-qwen35-zerodot8b-6a705b58-dc17/v1\",\"PersistVolumeName\":\"rayjob-20260804152823-ptbk-cos-34c3f2811e7c39a470e20081757ac1fd\",\"VolumeMountMode\":\"ReadOnly\",\"Source\":null,\"Origin\":null},{\"Region\":\"ap-guangzhou\",\"Bucket\":\"qzzhu-260200065\",\"VolumeSubPath\":\"/datasets/sft/train80\",\"SubPathMode\":null,\"SubPath\":null,\"MountPath\":\"/datasets/sft/train80\",\"PersistVolumeName\":\"rayjob-20260804152823-ptbk-cos-b2e28c1aee9d748a30406f7227b4f91d\",\"VolumeMountMode\":null,\"Source\":\"dataset\",\"Origin\":\"cos_reference\"},{\"Region\":\"ap-guangzhou\",\"Bucket\":\"qzzhu-260200065\",\"VolumeSubPath\":\"/checkpoints/sft/train80-v3\",\"SubPathMode\":null,\"SubPath\":null,\"MountPath\":\"/checkpoints/sft/train80\",\"PersistVolumeName\":\"rayjob-20260804152823-ptbk-cos-c078294231fc46b0d4b59bf5c6f0cf45\",\"VolumeMountMode\":\"ReadWrite\",\"Source\":\"checkpoint\",\"Origin\":null}],\"GooseFSVolumes\":null}",
                "CreateTime": 1785828503572,
                "Creator": "700002655693",
                "Entrypoint": "python /workspace/ray_post_training_entry.py --num-workers 1 --gpus-per-worker 1 --cpus-per-worker 20",
                "HistoryUrl": "https://test-tcray-historyserver-guangzhou.cloud.tencent.com/history/dlc-p-axzbtgug/rayjob-20260804152823-ptbk/jobs/rayjob-20260804152823-ptbk/",
                "Image": "ccr.ccs.tencentyun.com/emr-image/tcray:2.55.1-py311-cu125-torch2.10.0-tfm5.6",
                "InstanceId": "rayjob-20260804152823-ptbk",
                "JobCreateTime": 1785828511904,
                "JobRunningTime": 1045972,
                "Kind": "POST_TRAINING",
                "Mode": "sft",
                "Priority": 5,
                "Queue": "default",
                "ResourceConfig": "{\"Head\":{\"Name\":\"Head\",\"PodCpu\":1,\"PodMem\":4,\"GpuType\":\"\",\"GpuNum\":0,\"Envs\":[],\"Labels\":[],\"ResourcesLabels\":[],\"Tolerations\":null,\"ResourceType\":\"CPU\",\"InstanceType\":\"\",\"Spec\":1,\"BillingItem\":\"sv_dlc_standard_cu_standard_cu\",\"VideoMemory\":null,\"PodNum\":1,\"HighAvailability\":false,\"LabCu\":null},\"Worker\":[{\"Name\":\"WorkerGroup01\",\"PodCpu\":20,\"PodMem\":80,\"GpuType\":\"T4\",\"GpuNum\":1,\"Envs\":[],\"Labels\":[],\"ResourcesLabels\":[],\"Tolerations\":null,\"ResourceType\":\"GPU\",\"InstanceType\":\"GN7\",\"Spec\":1,\"BillingItem\":\"sv_dlc_gn7_gn75xlarge80\",\"VideoMemory\":null,\"MinPodNum\":1,\"MaxPodNum\":1,\"EnableAutoScaling\":false}]}",
                "ResourcePartitionId": "dlc-p-axzbtgug",
                "ResourcePartitionName": "gpu-t4",
                "RuntimeEnv": "{\"env_vars\":{\"TRAIN_CONFIG_YAML_B64\":\"IyDorq3nu4PphY3nva7vvJpTRlQgKOebkeedo+W+ruiwgykKIyDljaDkvY3nrKYgJHsuLi59IOeUsSBQb3N0VHJhaW5pbmdUZW1wbGF0ZVJlbmRlcmVyIOaMieeUqOaIt+ihqOWNlea4suafk+abv+aNouOAggojIOWOn+eUnyBIdWdnaW5nRmFjZSBUcmFpbmVyICsgdHJsLlNGVFRyYWluZXLvvIzkuI3kvp3otZYgTExhTUEtRmFjdG9yeeOAggoKIyMjIG1ldGhvZApzdGFnZTogc2Z0CmZpbmV0dW5pbmdfdHlwZTogbG9yYSAgICAgICAgICAgICAjIGZ1bGwgfCBsb3JhCmxvcmFfdGFyZ2V0OiBhbGwKbG9yYV9yYW5rOiA4CmxvcmFfYWxwaGE6IDE2CmxvcmFfZHJvcG91dDogMC4wNQoKIyMjIG1vZGVsCm1vZGVsX25hbWVfb3JfcGF0aDogL21vZGVscy9tLXF3ZW4zNS16ZXJvZG90OGItNmE3MDViNTgtZGMxNy92MQp0cnVzdF9yZW1vdGVfY29kZTogdHJ1ZQoKIyMjIGRhdGFzZXQKdHJhaW5fZmlsZTogICAgICAgICAgICAgICAgICAgICAgIyDmlbDmja7mlofku7blkI3miJbnu53lr7not6/lvoQKZGF0YXNldF9kaXI6IC9kYXRhc2V0cy9zZnQvdHJhaW44MApjdXRvZmZfbGVuOiA0MDk2Cm1heF9zYW1wbGVzOiAxMDAwMDAKcHJlcHJvY2Vzc2luZ19udW1fd29ya2VyczogMTYKCiMjIyBldmFsCmV2YWxfbW9kZTogc3BsaXQgICAgICAgICAgICAgICAgICAgICAgICMgbm9uZSB8IHNwbGl0IHwgc2VwYXJhdGUKZXZhbF9zcGxpdF9yYXRpbzogMC4wNiAgICAgICAgICAjIOS7hSBzcGxpdCDmqKHlvI/nlJ/mlYgKZXZhbF9maWxlOiAgICAgICAgICAgICAgICAgICAgICAgICAjIOS7hSBzZXBhcmF0ZSDmqKHlvI/nlJ/mlYgKZXZhbF9kYXRhc2V0X2RpcjogICAgICAgICAgICMg5LuFIHNlcGFyYXRlIOaooeW8j+eUn+aViAoKIyMjIG91dHB1dApvdXRwdXRfZGlyOiAvY2hlY2twb2ludHMvc2Z0L3RyYWluODAKIyDkuqflh7rmqKHlnovlkI3np7DvvIjnlKjkuo7lkI7nu63mqKHlnovms6jlhozvvIkKb3V0cHV0X21vZGVsX25hbWU6IApsb2dnaW5nX3N0ZXBzOiAxMApzYXZlX3N0cmF0ZWd5OiAiZXBvY2giCnNhdmVfc3RlcHM6IDEKc2F2ZV90b3RhbF9saW1pdDogMwojIOaWreeCuee7reiure+8mnRydWUg5pe25LuOIG91dHB1dF9kaXIg5Lit5pyA5pawIGNoZWNrcG9pbnQg5oGi5aSN6K6t57uDCnJlc3VtZV90cmFpbmluZzogZmFsc2UKIyDnlLHlubPlj7DmuLLmn5PvvIzlkK/nlKggTUxmbG93IOaXtuS4uiBbIm1sZmxvdyIsInRlbnNvcmJvYXJkIl3vvIzmnKrlkK/nlKjml7bkuLogdGVuc29yYm9hcmQKcmVwb3J0X3RvOiBbIm1sZmxvdyIsInRlbnNvcmJvYXJkIl0KcnVuX25hbWU6ICR7UlVOX05BTUV9CgojIyMgdHJhaW4KcGVyX2RldmljZV90cmFpbl9iYXRjaF9zaXplOiAxCmdyYWRpZW50X2FjY3VtdWxhdGlvbl9zdGVwczogNApncmFkaWVudF9jaGVja3BvaW50aW5nOiBmYWxzZQpsZWFybmluZ19yYXRlOiAxLjBFLTQKbnVtX3RyYWluX2Vwb2NoczogNApscl9zY2hlZHVsZXJfdHlwZTogY29zaW5lCndhcm11cF9yYXRpbzogMC4wMwpiZjE2OiB0cnVlCmRkcF90aW1lb3V0OiAxODAwMDAwMDAKCiMjIyBkZWVwc3BlZWQgKOa4suafk+e7k+aenOi3r+W+hO+8jOeUseWFpeWPo+iEmuacrCBiYXNlNjQg6Kej56CB5YaZ5Ye6KQpkZWVwc3BlZWQ6IC90bXAvdHJhaW4tY29uZmlnL2RzX3ozLmpzb24KCiMjIyBldmFsCnBlcl9kZXZpY2VfZXZhbF9iYXRjaF9zaXplOiAxCmV2YWxfc3RyYXRlZ3k6ICJlcG9jaCIgICAgICAgICAgICAgICAjICJubyIgfCAic3RlcHMiIHwgImVwb2NoIgpldmFsX3N0ZXBzOiA1MDAK\",\"DEEPSPEED_CONFIG_B64\":\"ewogICAgInRyYWluX2JhdGNoX3NpemUiOiAiYXV0byIsCiAgICAidHJhaW5fbWljcm9fYmF0Y2hfc2l6ZV9wZXJfZ3B1IjogImF1dG8iLAogICAgImJmMTYiOiB7ImVuYWJsZWQiOiAiYXV0byJ9LAogICAgImdyYWRpZW50X2NsaXBwaW5nIjogImF1dG8iLAogICAgInplcm9fb3B0aW1pemF0aW9uIjogewogICAgICAgICJvZmZsb2FkX29wdGltaXplciI6IHsiZGV2aWNlIjogIm5vbmUifSwKICAgICAgICAib3ZlcmxhcF9jb21tIjogdHJ1ZSwKICAgICAgICAic3RhZ2UiOiAzLAogICAgICAgICJzdWJfZ3JvdXBfc2l6ZSI6IDFFKzksCiAgICAgICAgImNvbnRpZ3VvdXNfZ3JhZGllbnRzIjogdHJ1ZSwKICAgICAgICAicmVkdWNlX2J1Y2tldF9zaXplIjogImF1dG8iLAogICAgICAgICJzdGFnZTNfZ2F0aGVyXzE2Yml0X3dlaWdodHNfb25fbW9kZWxfc2F2ZSI6IHRydWUsCiAgICAgICAgIm9mZmxvYWRfcGFyYW0iOiB7ImRldmljZSI6ICJub25lIn0sCiAgICAgICAgInN0YWdlM19wcmVmZXRjaF9idWNrZXRfc2l6ZSI6ICJhdXRvIiwKICAgICAgICAic3RhZ2UzX3BhcmFtX3BlcnNpc3RlbmNlX3RocmVzaG9sZCI6ICJhdXRvIiwKICAgICAgICAic3RhZ2UzX21heF9saXZlX3BhcmFtZXRlcnMiOiAxRSs5LAogICAgICAgICJzdGFnZTNfbWF4X3JldXNlX2Rpc3RhbmNlIjogMUUrOQogICAgfSwKICAgICJ6ZXJvX2FsbG93X3VudGVzdGVkX29wdGltaXplciI6IHRydWUsCiAgICAiZ3JhZGllbnRfYWNjdW11bGF0aW9uX3N0ZXBzIjogImF1dG8iLAogICAgImZwMTYiOiB7CiAgICAgICAgIm1pbl9sb3NzX3NjYWxlIjogMSwKICAgICAgICAiaW5pdGlhbF9zY2FsZV9wb3dlciI6IDE2LAogICAgICAgICJsb3NzX3NjYWxlIjogMCwKICAgICAgICAiZW5hYmxlZCI6ICJhdXRvIiwKICAgICAgICAibG9zc19zY2FsZV93aW5kb3ciOiAxMDAwLAogICAgICAgICJoeXN0ZXJlc2lzIjogMgogICAgfQp9Cg==\",\"NUM_WORKERS\":\"1\",\"GPUS_PER_WORKER\":\"1\",\"CPUS_PER_WORKER\":\"20\",\"NCCL_DEBUG\":\"WARN\",\"HF_HOME\":\"/workspace/cache/hf\",\"WANDB_DISABLED\":\"true\",\"MLFLOW_TRACKING_URI\":\"http://mlflow-7f72b80b-mlflow-svc.dlc-p-axzbtgug.svc.cluster.local:5000\",\"MLFLOW_EXPERIMENT_NAME\":\"sft-train80-qzzhu_checkpoints_v2_Clone\",\"MLFLOW_TAGS\":\"{\\\"job_id\\\":\\\"sft-train80-qzzhu_checkpoints_v2_Clone\\\",\\\"experiment_name\\\":\\\"sft-train80-qzzhu_checkpoints_v2_Clone\\\",\\\"mode\\\":\\\"sft\\\",\\\"finetune_type\\\":\\\"lora\\\",\\\"model\\\":\\\"v1\\\",\\\"source\\\":\\\"ray-nexus\\\"}\",\"HF_MLFLOW_LOG_ARTIFACTS\":\"false\",\"RAY_OVERRIDE_JOB_RUNTIME_ENV\":\"1\"}}",
                "SpecId": "raytrain-spec-tj8i36-q65j",
                "SpecName": "sft-train80-qzzhu_checkpoints_v2_Clone",
                "Status": "SUCCEEDED"
            }
        ],
        "Page": 1,
        "PageSize": 200,
        "Total": 22,
        "TotalPages": 1,
        "RequestId": "bb137fa3-26ee-4dd2-bab9-b9b627f814a1"
    }
}
```

