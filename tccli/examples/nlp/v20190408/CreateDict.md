**Example 1: 自定义词库创建接口示例**



Input: 

```
tccli nlp CreateDict --cli-unfold-argument  \
    --Description 王者荣耀4月份新增英雄人名 \
    --Name 王者荣耀人名
```

Output: 
```
{
    "Response": {
        "RequestId": "d9acba6d-bbb9-4e84-aaf3-0ced77ee83ff",
        "DictId": "udf-1b6b79e4cc"
    }
}
```

