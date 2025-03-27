**Example 1: 移动分类**

移动分类

Input: 

```
tccli cme MoveClass --cli-unfold-argument  \
    --Platform 1000000009 \
    --Owner.Type PERSON \
    --Owner.Id 9b92a8e7-a5ef-4e28-d72e-4eff571fabf0 \
    --SourceClassPath /媒资 \
    --DestinationClassPath /媒资/综艺 \
    --Operator 9b92a8e7-a5ef-4e28-d72e-4eff571fabf0
```

Output: 
```
{
    "Response": {
        "RequestId": "requestId"
    }
}
```

