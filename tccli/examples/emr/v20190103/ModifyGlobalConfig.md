**Example 1: 修改YARN资源调度的全局配置**



Input: 

```
tccli emr ModifyGlobalConfig --cli-unfold-argument  \
    --InstanceId abc \
    --Items.0.Key abc \
    --Items.0.Value abc
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

