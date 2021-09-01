**Example 1: 列出所有集群内模型**



Input: 

```
tccli tia ListModels --cli-unfold-argument  \
    --Cluster ap-beijing
```

Output: 
```
{
    "Response": {
        "Models": [
            {
                "Name": "test-model-2",
                "Description": "test",
                "Cluster": "test",
                "Model": "cos://tia-demo-1255502019.cos.ap-shanghai.myqcloud.com/mnist_example:/data/mnist",
                "RuntimeVersion": "tiaserv-1.6.0-cpu",
                "CreateTime": "2018-09-19 11:19:58 +0800 CST",
                "State": "Running",
                "ServingUrl": "140.143.114.17",
                "Message": "Deployment has minimum availability.",
                "Replicas": 0,
                "AppId": 1254139681,
                "Expose": "",
                "ServType": "1U2G0P"
            },
            {
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
            }
        ],
        "RequestId": "af499c6b-5f40-4e9c-a8eb-7df4e85cbf60"
    }
}
```

**Example 2: 列出所有 SCF 模型**



Input: 

```
tccli tia ListModels --cli-unfold-argument  \
    --Cluster test \
    --ServType serverless
```

Output: 
```
{
    "Response": {
        "Models": [
            {
                "Name": "scf-test-model-0",
                "Description": "",
                "Cluster": "",
                "Model": "",
                "RuntimeVersion": "Python2.7",
                "CreateTime": "2018-09-12 20:26:02",
                "State": "",
                "ServingUrl": "",
                "Message": "",
                "Replicas": 0,
                "AppId": 0,
                "Expose": "",
                "ServType": ""
            },
            {
                "Name": "scf-test-model-2",
                "Description": "",
                "Cluster": "",
                "Model": "",
                "RuntimeVersion": "Python2.7",
                "CreateTime": "2018-09-12 20:25:55",
                "State": "",
                "ServingUrl": "",
                "Message": "",
                "Replicas": 0,
                "AppId": 0,
                "Expose": "",
                "ServType": ""
            }
        ],
        "RequestId": "a03d3814-1ea3-4bfd-8271-8ff717fd0d3e"
    }
}
```

