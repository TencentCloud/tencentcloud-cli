**Example 1: 选取一个模型部署服务到集群中**

在名为 ap-beijing 的集群上运行一个名为 test-model 的模型，对外提供服务。使用预提供的标签为 tiaserv-1.6.0-cpu 的运行环境，指定机器配置为：4核CPU，8G内存，不使用GPU。

Input: 

```
tccli tia CreateModel --cli-unfold-argument  \
    --Name test-model \
    --Description test \
    --Cluster ap-beijing \
    --Model cos://bucket-xxxxxxxxxx.cos.ap-guangzhou.myqcloud.com/model:/data/model \
    --RuntimeVersion tiaserv-1.6.0-cpu \
    --Replicas 1 \
    --Expose external \
    --ServType 4U8G0P
```

Output: 
```
{
    "Response": {
        "Model": {
            "Name": "test-model",
            "Description": "test",
            "Cluster": "ap-beijing",
            "Model": "cos://bucket-xxxxxxxxxx.cos.ap-guangzhou.myqcloud.com/model:/data/model",
            "RuntimeVersion": "tiaserv-1.6.0-cpu",
            "CreateTime": "2018-05-23 10:00:00 +0800 CST",
            "State": "",
            "Message": "creating",
            "Replicas": 1,
            "AppId": "xxxxxxxxxx",
            "Expose": "external",
            "ServType": ""
        },
        "RequestId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    }
}
```

**Example 2: 选取一个模型采用无服务器函数的方式部署**

读取 cos 上以 *.zip 格式打包好的代码文件，部署为一个无服务器函数。运行环境为 Python2.7，脚本执行入口为 mnist.apigw_interface，请求的运行环境内存大小为 1024Gb，运行设置最大等待时间为 10 秒。

Input: 

```
tccli tia CreateModel --cli-unfold-argument  \
    --Name test-model \
    --Description test \
    --Model cos://bucket-xxxxxxxxxx.cos.ap-guangzhou.myqcloud.com/model.zip \
    --RuntimeVersion Python2.7 \
    --ServType serverless \
    --RuntimeConf Handler MemorySize Timeout
```

Output: 
```
{
    "Response": {
        "Model": {
            "Name": "test-model",
            "Description": "test",
            "Cluster": "",
            "Model": "cos://bucket-xxxxxxxxxx.cos.ap-guangzhou.myqcloud.com/model.zip",
            "RuntimeVersion": "",
            "CreateTime": "Wednesday, 19-Sep-18 11:01:29 CST",
            "State": "Ready",
            "ServingUrl": "",
            "Message": "",
            "Replicas": 0,
            "AppId": "xxxxxxxxxx",
            "Expose": "",
            "ServType": "serverless"
        },
        "RequestId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    }
}
```

