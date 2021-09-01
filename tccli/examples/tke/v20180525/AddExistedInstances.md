**Example 1: 添加已经存在的实例到集群**

添加已经存在的实例到集群

Input: 

```
tccli tke AddExistedInstances --cli-unfold-argument  \
    --ClusterId cls-xxxxxx \
    --InstanceIds ins-xxxxx
```

Output: 
```
{
    "Response": {
        "TimeoutInstanceIds": [
            "ins-lqdahrp3"
        ],
        "SuccInstanceIds": [
            "ins-lqdahrp4"
        ],
        "FailedInstanceIds": [
            "ins-lqdahrp5"
        ],
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "FailedReasons": [
            "InstanceId ins-lqdahrp5 ServiceResetCvmV3 failed ..."
        ]
    }
}
```

