**Example 1: 获取弱口令配置**

获取弱口令配置

Input: 

```
tccli csip DescribeBaselineUserWeakPasswordConf --cli-unfold-argument  \
    --MemberId mem-**n*********95752f66e429
```

Output: 
```
{
    "Response": {
        "UserConf": "sqwu",
        "RequestId": "572a143f-9809-47a7-8d17-ef592a3a54bf"
    }
}
```

