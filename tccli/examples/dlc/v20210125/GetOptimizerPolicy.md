**Example 1: test**



Input: 

```
tccli dlc GetOptimizerPolicy --cli-unfold-argument  \
    --SmartPolicy.BaseInfo.Uin abc \
    --SmartPolicy.BaseInfo.PolicyType abc \
    --SmartPolicy.BaseInfo.Catalog abc \
    --SmartPolicy.BaseInfo.Database abc \
    --SmartPolicy.BaseInfo.Table abc \
    --SmartPolicy.BaseInfo.AppId abc \
    --SmartPolicy.Policy.Inherit abc \
    --SmartPolicy.Policy.Resources.0.AttributionType abc \
    --SmartPolicy.Policy.Resources.0.ResourceType abc \
    --SmartPolicy.Policy.Resources.0.Name abc \
    --SmartPolicy.Policy.Resources.0.Instance abc \
    --SmartPolicy.Policy.Resources.0.Favor.0.Priority 0 \
    --SmartPolicy.Policy.Resources.0.Favor.0.Catalog abc \
    --SmartPolicy.Policy.Resources.0.Favor.0.DataBase abc \
    --SmartPolicy.Policy.Resources.0.Favor.0.Table abc \
    --SmartPolicy.Policy.Resources.0.Status 0 \
    --SmartPolicy.Policy.Lifecycle.LifecycleEnable abc \
    --SmartPolicy.Policy.Lifecycle.Expiration 0 \
    --SmartPolicy.Policy.Lifecycle.DropTable True \
    --SmartPolicy.Policy.Index.IndexEnable abc
```

Output: 
```
{
    "Response": {
        "SmartOptimizerPolicy": {
            "Inherit": "abc",
            "Resources": [
                {
                    "AttributionType": "abc",
                    "ResourceType": "abc",
                    "Name": "abc",
                    "Instance": "abc",
                    "Favor": [
                        {
                            "Priority": 0,
                            "Catalog": "abc",
                            "DataBase": "abc",
                            "Table": "abc"
                        }
                    ],
                    "Status": 0
                }
            ],
            "Written": {},
            "Lifecycle": {
                "LifecycleEnable": "abc",
                "Expiration": 0,
                "DropTable": true
            },
            "Index": {
                "IndexEnable": "abc"
            }
        },
        "RequestId": "abc"
    }
}
```

