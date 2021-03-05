**Example 1: 调用失败示例**



Input: 

```
tccli bda ModifyGroup --cli-unfold-argument  \
    --GroupId 12312312 \
    --GroupName testG3M3 \
    --Tag testG3M3
```

Output: 
```
{
    "Response": {
        "RequestId": "3661682c-414a-48d0-86fd-939d504bab70"
    }
}
```

**Example 2: 调用成功示例**



Input: 

```
tccli bda ModifyGroup --cli-unfold-argument  \
    --GroupId testG3 \
    --GroupName testG3M3 \
    --Tag testG3M3
```

Output: 
```
{
    "Response": {
        "RequestId": "32ac4a6a-7a58-4968-b32e-b8d7772eb26e"
    }
}
```

