**Example 1: 删除集群中的实例**

删除集群中的实例

Input: 

```
tccli tke DeleteClusterInstances --cli-unfold-argument  \
    --ClusterId cls-7ph3twqe \
    --InstanceIds ins-1w67yfj8 \
    --InstanceDeleteMode terminate
```

Output: 
```
{
    "Response": {
        "SuccInstanceIds": [
            "ins-1w67yfj8"
        ],
        "FailedInstanceIds": [
            "ins-1w67yfj9"
        ],
        "NotFoundInstanceIds": [
            "ins-1w67yfj0"
        ],
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

