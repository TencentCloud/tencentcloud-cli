**Example 1: 查询serverless策略**



Input: 

```
tccli cynosdb DescribeServerlessStrategy --cli-unfold-argument  \
    --ClusterId cynosdbmysql-xxx
```

Output: 
```
{
    "Response": {
        "AutoPauseDelay": 300,
        "AutoScaleDownDelay": 60,
        "AutoPause": "yes",
        "RequestId": "8727691c-3536-11eb-81e7-525400b7dd5a",
        "AutoScaleUpDelay": 30
    }
}
```

