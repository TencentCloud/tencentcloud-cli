**Example 1: 示例**



Input: 

```
tccli tchousex AddSparkJob --cli-unfold-argument  \
    --Files cosn://test-cq/test.jar \
    --PyFiles cosn://test-cq/pi.py \
    --ExecutorNum 1 \
    --SparkName xx \
    --InstanceId xx \
    --Args xx \
    --ClassName xx \
    --Archives xx \
    --File xx \
    --ExecutorCores 1 \
    --DriverCores 1 \
    --Configs xx \
    --Jars xx
```

Output: 
```
{
    "Response": {
        "RequestId": "tueye-123ytt-443frt"
    }
}
```

