**Example 1: GetLabEvent**

获取实验室事件

Input: 

```
tccli dlc GetLabEvent --cli-unfold-argument  \
    --Id raylab-20260602161511-uu7l \
    --PageSize 1 \
    --StartTime 178432543543 \
    --EndTime 178478354353
```

Output: 
```
{
    "Response": {
        "Events": [],
        "ListOver": true,
        "RequestId": "f377fc09-b8f1-42ea-90e9-a59ab19b36fa"
    }
}
```

