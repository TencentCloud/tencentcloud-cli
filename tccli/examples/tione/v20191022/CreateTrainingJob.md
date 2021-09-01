**Example 1: 创建一个训练任务**



Input: 

```
tccli tione CreateTrainingJob --cli-unfold-argument  \
    --TrainingJobName test \
    --HyperParameters {"learning_rate":1.0} \
    --AlgorithmSpecification.TrainingImageName ccr.ccs.tencentyun.com/ti_public/tensorflow:1.14.0-py3 \
    --AlgorithmSpecification.TrainingInputMode File \
    --OutputDataConfig.CosOutputBucket bucket \
    --OutputDataConfig.CosOutputKeyPrefix test \
    --ResourceConfig.InstanceCount 1 \
    --ResourceConfig.InstanceType TI.SMALL2.1core2g \
    --ResourceConfig.VolumeSizeInGB 10 \
    --InputDataConfig.0.ChannelName train \
    --InputDataConfig.0.DataSource.CosDataSource.Bucket bucket \
    --InputDataConfig.0.DataSource.CosDataSource.KeyPrefix test \
    --InputDataConfig.0.InputMode File
```

Output: 
```
{
    "Response": {
        "RequestId": "89719e50-4e38-4287-9205-00afcf4dd780",
        "TrainingJobName": "test"
    }
}
```

