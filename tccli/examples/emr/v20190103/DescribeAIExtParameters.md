**Example 1: 实例1**



Input: 

```
tccli emr DescribeAIExtParameters --cli-unfold-argument  \
    --InstanceId emr-j9lwlphp \
    --JobType PySpark \
    --SceneType Offline
```

Output: 
```
{
    "Response": {
        "ParametersList": [
            {
                "ConfName": "spark.driver.cores",
                "ConfValue": "2"
            }
        ],
        "RequestId": "4f051c5e-2df0-4f84-9237-1e18109b3c35"
    }
}
```

