**Example 1: 人员查重接口调用成功**



Input: 

```
tccli iai CheckSimilarPerson --cli-unfold-argument  \
    --UniquePersonControl 1 \
    --GroupIds MyGroup1 MyGroup2
```

Output: 
```
{
    "Response": {
        "JobId": "YP6v5v32pvyBqLyz",
        "RequestId": "5cec97ca-4a86-466b-a437-82df71d625a7"
    }
}
```

**Example 2: 人员查重接口调用失败**



Input: 

```
tccli iai CheckSimilarPerson --cli-unfold-argument  \
    --UniquePersonControl 1 \
    --GroupIds MyGroup11111 MyGroup22222
```

Output: 
```
{
    "Response": {
        "RequestId": "f08f36f9-671f-4448-a973-dae899aaeb10"
    }
}
```

