**Example 1: 调用失败示例**



Input: 

```
tccli bda CreateGroup --cli-unfold-argument  \
    --GroupName testG3 \
    --GroupId testG3 \
    --Tag TestG3T3 \
    --BodyModelVersion 2.0
```

Output: 
```
{
    "Response": {
        "RequestId": "e1d5929c-5d72-4b2a-b354-2767056a6929"
    }
}
```

**Example 2: 调用成功示例**



Input: 

```
tccli bda CreateGroup --cli-unfold-argument  \
    --GroupName testG3 \
    --GroupId testG3 \
    --Tag TestG3T3 \
    --BodyModelVersion 1.0
```

Output: 
```
{
    "Response": {
        "RequestId": "95d7ed2b-4f54-4952-96d0-995981981e37"
    }
}
```

