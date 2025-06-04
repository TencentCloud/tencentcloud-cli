**Example 1: 示例**

示例

Input: 

```
tccli gs ModifyAndroidInstancesProperties --cli-unfold-argument  \
    --AndroidInstanceIds cai-251006279-ea99wkeEIID cai-251006279-ea99NQV3Qw7 \
    --AndroidInstanceDevice.Brand google \
    --AndroidInstanceDevice.Model Pixel3 \
    --AndroidInstanceProperties.0.Key testkey \
    --AndroidInstanceProperties.0.Value testvalue
```

Output: 
```
{
    "Response": {
        "RequestId": "16152a6a-d031-4506-8eba-466e6a286c01"
    }
}
```

