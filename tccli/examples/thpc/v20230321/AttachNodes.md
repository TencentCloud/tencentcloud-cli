**Example 1: 绑定计算节点到集群**

往集群ID为hpc-2j8ntf9l的集群的compute队列绑定一个计算节点。

Input: 

```
tccli thpc AttachNodes --cli-unfold-argument  \
    --ClusterId hpc-2j8ntf9l \
    --QueueName compute \
    --ImageId img-39ywauzd \
    --ResourceType CVM \
    --ResourceSet ins-7i4yut4b
```

Output: 
```
{
    "Response": {
        "RequestId": "e81d404b-4fa2-49de-bce7-6499a3529f04"
    }
}
```

