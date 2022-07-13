**Example 1: 修改Logstash实例名称**

用以修改指定Logstash实例的名称

Input: 

```
tccli es UpdateLogstashInstance --cli-unfold-argument  \
    --InstanceId ls-xxxxxx \
    --InstanceName newName
```

Output: 
```
{
    "Response": {
        "RequestId": "c96a110c-7493-452d-a99b-683d07xxxxxx"
    }
}
```

