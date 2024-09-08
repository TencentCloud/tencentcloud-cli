**Example 1: yarn资源调度-重置**

取消修改的配置

Input: 

```
tccli emr ResetYarnConfig --cli-unfold-argument  \
    --InstanceId emr-xxx \
    --Key fair
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

