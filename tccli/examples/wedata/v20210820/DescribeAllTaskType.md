**Example 1: 样例**

获取任务类型

Input: 

```
tccli wedata DescribeAllTaskType --cli-unfold-argument  \
    --ProjectId 1460947878944567296
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "TypeDesc": "JDBC SQL",
                "TypeId": 21,
                "TypeSort": "数据计算"
            }
        ],
        "RequestId": "d197a658-411e-4d82-a3f6-35b11e5c9c44"
    }
}
```

