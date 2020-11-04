**Example 1: 查询环境个数上限接口**



Input: 

```
tccli tcb DescribeEnvLimit --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "MaxEnvNum": 0,
        "CurrentEnvNum": 0,
        "MaxFreeEnvNum": 0,
        "CurrentFreeEnvNum": 0,
        "MaxDeleteTotal": 0,
        "CurrentDeleteTotal": 0,
        "MaxDeleteMonthly": 0,
        "CurrentDeleteMonthly": 0,
        "RequestId": "046cacfd-af90-4355-ac92-f56954bd1831"
    }
}
```

