**Example 1: 测试样例**

查询1460947878944567296项目的周期任务分布

Input: 

```
tccli wedata DescribeTaskByCycle --cli-unfold-argument  \
    --ProjectId 1460947878944567296
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Number": 1,
                "CycleUnit": "D",
                "ProjectId": "1460947878944567296"
            }
        ],
        "RequestId": "f6aaa583-9ce1-4e92-a183-ea90a2a49d1d"
    }
}
```

**Example 2: 1**

1

Input: 

```
tccli wedata DescribeTaskByCycle --cli-unfold-argument  \
    --ProjectId 1 \
    --InCharge 1
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "UnknownParameter",
            "Message": "The parameter `InCharge` is not recognized."
        },
        "RequestId": "abf5e263-d72f-422b-b38f-5c484bd1238a"
    }
}
```

