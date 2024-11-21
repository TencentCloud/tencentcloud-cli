**Example 1: yarn资源调度-重置**

取消修改的配置

Input: 

```
tccli emr ResetYarnConfig --cli-unfold-argument  \
    --InstanceId emr-1si \
    --Key fair
```

Output: 
```
{
    "Response": {
        "RequestId": "28026cdd-41a9-4433-a80d-673ec711bca8"
    }
}
```

