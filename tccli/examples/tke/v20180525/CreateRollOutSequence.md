**Example 1: 创建发布序列**

创建一个集群发布序列

Input: 

```
tccli tke CreateRollOutSequence --cli-unfold-argument  \
    --Name test1 \
    --SequenceFlows.0.Tags Test \
    --SequenceFlows.0.SoakTime 86400 \
    --SequenceFlows.1.Tags Pre-Production \
    --SequenceFlows.1.SoakTime 86400 \
    --SequenceFlows.2.Tags Production \
    --SequenceFlows.2.SoakTime 86400 \
    --Enabled True
```

Output: 
```
{
    "Response": {
        "RequestId": "f1048559-c7e4-4a7b-9d12-bc0256be3e26"
    }
}
```

