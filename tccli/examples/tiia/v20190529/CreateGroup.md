**Example 1: 调用成功示例**

调用成功示例

Input: 

```
tccli tiia CreateGroup --cli-unfold-argument  \
    --Brief brief_test \
    --GroupName name_test \
    --MaxQps 10 \
    --MaxCapacity 100 \
    --GroupId test_group
```

Output: 
```
{
    "Response": {
        "RequestId": "7ba53193-90af-4440-b706-b3d3a0657982"
    }
}
```

