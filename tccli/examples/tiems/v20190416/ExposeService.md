**Example 1: 暴露模型服务**



Input: 

```
tccli tiems ExposeService --cli-unfold-argument  \
    --ServiceId ank95gbm4dwfhmds \
    --ExposeType EXTERNAL
```

Output: 
```
{
    "Response": {
        "RequestId": "2b6049dc-f99a-47e9-99fa-f701ecc4b76a",
        "Expose": {
            "ExposeType": "EXTERNAL",
            "VpcId": "",
            "SubnetId": "",
            "Ip": "pending"
        }
    }
}
```

