**Example 1: 创建token**

生产的时候clentId带上token 可以绕过acl(需要提工单升级broker版本)

Input: 

```
tccli ckafka CreateToken --cli-unfold-argument  \
    --User testUser \
    --InstanceId ckafka-xxxasa
```

Output: 
```
{
    "Response": {
        "Result": "904b75130b4b4102bdeb071a7f48523a",
        "RequestId": "20e995ed-75b9-43bb-84c0-35676567e1a8"
    }
}
```

