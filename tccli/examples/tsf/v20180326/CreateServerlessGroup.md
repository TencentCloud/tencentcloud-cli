**Example 1: 创建Serverless部署组**

创建Serverless部署组

Input: 

```
tccli tsf CreateServerlessGroup --cli-unfold-argument  \
    --ApplicationId application-xxxxxxx \
    --GroupName consumer \
    --NamespaceId namespace-xxxxxxxx \
    --ClusterId cluster-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "39bb8e88-1ccd-4204-9f9e-56804c980a31",
        "Result": "group-xxxxxxx"
    }
}
```

