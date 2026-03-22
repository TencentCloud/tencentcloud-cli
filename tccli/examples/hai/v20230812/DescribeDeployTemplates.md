**Example 1: DescribeDeployTemplates**



Input: 

```
tccli hai DescribeDeployTemplates --cli-unfold-argument  \
    --ModelId mdl-nbb23f5v
```

Output: 
```
{
    "Response": {
        "EngineTypes": [
            "Sglang"
        ],
        "RequestId": "8835934f-5769-4df6-b1e4-0a36236d4968",
        "TemplateSet": [
            {
                "ComputeSet": [
                    {
                        "BundleType": "96G_A",
                        "CPU": "16",
                        "Count": 2,
                        "GPUCount": 1,
                        "GPUMemory": "96",
                        "GPUPerformance": "88 tflops++",
                        "Memory": "160"
                    }
                ],
                "DeployMode": "DISTRIBUTED",
                "EngineType": "Sglang",
                "TemplateId": "tpl-0j2qaa8t"
            }
        ]
    }
}
```

