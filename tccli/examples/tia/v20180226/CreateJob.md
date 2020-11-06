**Example 1: 创建一个训练任务**

在名为 ap-beijing 的集群上创建一个名为 test-job 的分布式任务。采用一个 master 节点，一个 ps 节点，和两个 worker 节点的计算节点结构，使用预提供的标签为 tia-1.7.0 的运行环境。

Input: 

```
tccli tia CreateJob --cli-unfold-argument  \
    --Name test-job \
    --Cluster ap-beijing \
    --RuntimeVersion tia-1.7.0 \
    --ScaleTier CUSTOM \
    --MasterType 1U1G0P \
    --WorkerType 1U1G0P \
    --ParameterServerType 1U1G0P \
    --WorkerCount 2 \
    --ParameterServerCount 1 \
    --Debug false \
    --PackageDir '/* nfs or cos address */' \
    --Command python \
    --Args mnist_saved_model.py
```

Output: 
```
{
    "Response": {
        "Job": {
            "Name": "test-job",
            "CreateTime": "2018-05-23 10:00:00.000000000 +0800 CST m=+66666.666666666",
            "Message": "creating",
            "ScaleTier": "Custom",
            "MasterType": "1U1G0P",
            "WorkerType": "1U1G0P",
            "ParameterServerType": "1U1G0P",
            "WorkerCount": 2,
            "ParameterServerCount": 1,
            "Debug": false,
            "PackageDir": [
                "/* nfs or cos address */"
            ],
            "Command": [
                "python"
            ],
            "Args": [
                "mnist_saved_model.py"
            ],
            "Cluster": "ap-beijing",
            "RuntimeVersion": "tia-1.7.0"
        },
        "RequestId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    }
}
```

