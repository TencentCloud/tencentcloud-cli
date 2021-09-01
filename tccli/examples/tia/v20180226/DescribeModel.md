**Example 1: 描述一个集群内模型的详细信息**



Input: 

```
tccli tia DescribeModel --cli-unfold-argument  \
    --Name test-model \
    --Cluster ap-beijing
```

Output: 
```
{
    "Response": {
        "Model": {
            "Name": "test-model",
            "Description": "test",
            "Cluster": "test",
            "Model": "cos://tia-demo-1255502019.cos.ap-shanghai.myqcloud.com/mnist_example:/data/mnist",
            "RuntimeVersion": "tiaserv-1.6.0-cpu",
            "CreateTime": "2018-09-19 11:18:19 +0800 CST",
            "State": "Running",
            "ServingUrl": "140.143.181.246",
            "Message": "Deployment has minimum availability.",
            "Replicas": 0,
            "AppId": 1254139681,
            "Expose": "",
            "ServType": "1U2G0P"
        },
        "RequestId": "daaecaca-46fb-47c7-ad4b-37387ec1ae09"
    }
}
```

**Example 2: 描述一个 SCF 模型的详细信息**



Input: 

```
tccli tia DescribeModel --cli-unfold-argument  \
    --Name scf-test-model-1 \
    --ServType serverless
```

Output: 
```
{
    "Response": {
        "Model": {
            "Name": "scf-test-model-1",
            "Description": "SCF model test.",
            "Cluster": "",
            "Model": "",
            "RuntimeVersion": "Python2.7",
            "CreateTime": "2018-09-12 20:26:02",
            "State": "Ready",
            "ServingUrl": "",
            "Message": "",
            "Replicas": 0,
            "AppId": 0,
            "Expose": "",
            "ServType": ""
        },
        "RequestId": "4cbcc08a-d490-42c5-8ff6-f4549af710f1"
    }
}
```

