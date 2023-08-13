**Example 1: 为应用创建组件**

为应用创建组件

Input: 

```
tccli camp CreateComponent --cli-unfold-argument  \
    --ApplicationID app-xxxx \
    --ProjectID prj-xxxx \
    --InstanceID ins-xxxx \
    --Component.Name test \
    --Component.Type k8s-objects \
    --Component.Properties.K8sObjects {}
```

Output: 
```
{
    "Response": {
        "RequestId": "67580ea3-66a3-4826-a589-6fa567ed544e"
    }
}
```

