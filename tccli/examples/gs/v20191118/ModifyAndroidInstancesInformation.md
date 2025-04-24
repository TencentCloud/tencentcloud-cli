**Example 1: 批量修改安卓实例信息**



Input: 

```
tccli gs ModifyAndroidInstancesInformation --cli-unfold-argument  \
    --AndroidInstanceInformations.0.AndroidInstanceId cai-251006279-ea99cM7rbg6 \
    --AndroidInstanceInformations.0.Name test_name
```

Output: 
```
{
    "Response": {
        "RequestId": "9207f7b7-06a0-44fc-932a-6a95baf7164e"
    }
}
```

