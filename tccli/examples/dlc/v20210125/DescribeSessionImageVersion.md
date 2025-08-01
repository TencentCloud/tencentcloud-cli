**Example 1: 内置镜像**

当前引擎：DataEngine-b0jt6fvk
框架类型选择：machine-learning

Input: 

```
tccli dlc DescribeSessionImageVersion --cli-unfold-argument  \
    --DataEngineId DataEngine-b0jt6fvk \
    --FrameworkType machine-learning
```

Output: 
```
{
    "Response": {
        "EngineSessionImages": [
            {
                "SparkImageId": "123e4567-e89b-12d3-a456-426614174001",
                "SparkImageTag": "ccr.ccs.tencentyun.com/dlc_cloud/tensorflow:dev-v20241218",
                "SparkImageType": 1,
                "SparkImageVersion": "tensorflow-v2.18.0"
            },
            {
                "SparkImageId": "1a2b3c4d-5e6f-7g8h-9i0j-k1l2m3n4o5p6",
                "SparkImageTag": "ccr.ccs.tencentyun.com/dlc_cloud/scikit-learn:dev-v20241218",
                "SparkImageType": 1,
                "SparkImageVersion": "scikit-learn-v1.6.0"
            },
            {
                "SparkImageId": "98765432-10fe-bcd1-9a8b-0123456789ab",
                "SparkImageTag": "ccr.ccs.tencentyun.com/dlc_cloud/pytorch:dev-v20241218",
                "SparkImageType": 1,
                "SparkImageVersion": "pytorch-v2.5.1"
            }
        ],
        "RequestId": "c06478c4-bbc6-4cec-934b-6f9e2ff121ae"
    }
}
```

