**Example 1: DPO LoRA 均衡模式**



Input: 

```
tccli dlc DescribePostTrainingPreset --cli-unfold-argument  \
    --Mode dpo \
    --TrainingMode balanced \
    --FineTuneType lora \
    --ParameterSize 8
```

Output: 
```
{
    "Response": {
        "Resource": {
            "Head": {
                "GpuNum": 0,
                "GpuType": "",
                "Name": "head",
                "PodCpu": 2,
                "PodMem": 8,
                "PodNum": 1,
                "ResourceType": "CPU",
                "Spec": 1
            },
            "Worker": [
                {
                    "GpuNum": 2,
                    "GpuType": "A100",
                    "MaxPodNum": 1,
                    "MinPodNum": 1,
                    "Name": "worker",
                    "PodCpu": 4,
                    "PodMem": 16,
                    "ResourceType": "GPU",
                    "Spec": 1
                }
            ]
        },
        "TrainingParams": {
            "CutoffLen": 4096,
            "Epochs": 3,
            "GradientAccumulationSteps": 4,
            "GradientCheckpointing": true,
            "LearningRate": 0.0001,
            "LoraRank": 8,
            "PerDeviceBatchSize": 2,
            "WarmupRatio": 0.03
        },
        "RequestId": "700c3a3d-7b35-4984-8614-8c628781e073"
    }
}
```

