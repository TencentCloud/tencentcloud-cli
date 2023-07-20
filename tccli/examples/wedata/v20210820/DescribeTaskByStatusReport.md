**Example 1: 样例**

查询1460947878944567296项目12小时的任务状态趋势

Input: 

```
tccli wedata DescribeTaskByStatusReport --cli-unfold-argument  \
    --Type 12h \
    --TaskType 30 \
    --TypeName Python \
    --ProjectId 1460947878944567296
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "CountGroup": "[17]",
                "ShowTimeGroup": "[20130101]",
                "Status": "F"
            }
        ],
        "RequestId": "8dd77dee-9a4c-40a8-8d00-00c0b1c05c9b"
    }
}
```

