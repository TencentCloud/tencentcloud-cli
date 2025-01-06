**Example 1: 删除函数指定版本**

删除函数 test 的版本 2 

Input: 

```
tccli scf DeleteFunctionVersion --cli-unfold-argument  \
    --FunctionName functionName1 \
    --Namespace default \
    --Qualifier 2
```

Output: 
```
{
    "Response": {
        "RequestId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    }
}
```

